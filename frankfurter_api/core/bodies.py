"""Request bodies: the wire shapes a transport receives, and the factories that build them.

A body is already serialized by the time it exists. Each factory validates the value against the
type the endpoint declared, dumps it through that type's adapter, and returns a frozen shape holding
nothing but wire-ready primitives -- so a transport, including a caller-supplied one, never
serializes anything, and :class:`HttpRequest` never carries a pydantic adapter.

``RequestBody`` is a closed union rather than a Protocol: all three shapes live here and are
generator-emitted, so the set cannot grow behind the runtime's back.

No operation in the current spec exercises :class:`MultipartBody`; it is kept because the capability
is part of the runtime's contract, not because a spec happens to use it today."""

from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Final, Generic, TypeAlias, TypeVar

from typing_extensions import TypeForm

from ._internal.flattening import to_fields
from .adapters import adapter_for, validation_target
from .optionality import strip_unset
from .params import Param

T = TypeVar("T")


@dataclass(frozen=True, slots=True)
class JsonBody(Generic[T]):
    """A JSON body of declared type ``T``, reduced to JSON-safe Python objects.

    ``T`` records the type the value was validated and dumped *as*; ``value`` holds the result of
    that dump, which is why it is ``object`` and not ``T``. Construct it through
    ``json_body[...]``, whose subscript is where ``T`` is bound."""

    value: object


@dataclass(frozen=True, slots=True)
class FormBody:
    """A url-encoded form body, already flattened into wire fields.

    A field is one text or, where the key repeats, the list of texts it collected -- the whole
    value space :func:`to_fields` can produce, spelled out so a caller-supplied transport is
    type-checked on what it does with them."""

    fields: Mapping[str, str | list[str]]


@dataclass(frozen=True, slots=True)
class MultipartBody:
    """A multipart body: flattened form fields alongside files.

    ``fields`` carries the same text-or-list-of-text values as :class:`FormBody`. ``files`` stays
    ``Any`` because its value space is genuinely open -- bytes, a file object, or a
    ``(filename, content, content_type)`` tuple, whatever the transport's library accepts."""

    fields: Mapping[str, str | list[str]]
    files: Mapping[str, Any]


RequestBody: TypeAlias = JsonBody[Any] | FormBody | MultipartBody
"""The body an endpoint hands to ``execute`` -- exactly one of the three shapes above.

A union rather than one class with three optional fields: of the eight combinations such a class
would admit, only three are legal, and the illegal five had to be rejected at runtime. Here they
cannot be written down. A transport ``match``es on this to pick its body arguments."""


class _JsonBodyFactory:
    """``json_body[T](value)`` -- name the body's declared type in the subscript.

    **A subscript and then a call, and the split is the whole point.** ``T`` is solved from the
    subscript alone, *before* the value is compared against it, which is what makes a generator
    emitting the wrong type a build failure: ``json_body[int](employee)`` is rejected with
    ``Argument 1 has incompatible type "Employee | EmployeeDict"; expected "int"``. Written as one
    call it could not be: ``json_body(employee, int)`` makes mypy solve ``T`` from *both*
    arguments and join them to ``object``, so every mismatch type-checks -- measured, along with
    the other shapes that fail the same way, in ADR-0013 (whose curried spelling this subscript
    replaced; the re-measurement is in docs/plans/subscripted-typed-factories.md).

    The factory declares no ``__call__``, so *omitting* the declared type is a build failure too:
    ``json_body(employee)`` is rejected statically (``[operator]``) -- the guarantee the curried
    signature used to carry. The runtime ``__call__`` below is invisible to type checkers and
    exists only to turn that same mistake into a guided ``TypeError``.

    The subscript is a ``TypeForm``, exactly as in ``json_decoder[...]``, so a runtime union alias
    (``Person``, which is ``Employee | Boss``) binds ``T`` as precisely as a concrete class does.

    The subscript is the endpoint's declared parameter type **in full**, dict-shaped companion
    included: ``json_body[Employee | EmployeeDict]``. The accepted value is then exactly ``T``, so
    there is no permissive mapping half for a stray ``dict[str, Any]`` to slip through -- and only
    the model arm reaches :func:`adapter_for`, via :func:`validation_target`, because a companion
    is an input shape and never a wire shape.

    Handles scalars, dicts, lists and nested structures, and honours ``Annotated`` serializers
    (``PlainSerializer`` and friends) because serialization goes through the type's own adapter.
    Validation runs before the dump, so dict-shaped input is coerced into the model through its own
    validation; a model instance passes through unchanged (``revalidate_instances`` defaults to
    ``"never"``), making this byte-identical for non-dict values. ``strip_unset`` then distinguishes
    a field the caller never touched (``OptionalNullable[...] = UNSET``, omitted) from one set
    explicitly to ``None`` (kept as null) -- see docs/designs/optional-nullable-fields.md."""

    def __getitem__(self, declared: TypeForm[T]) -> Callable[[T], JsonBody[T]]:
        adapter = adapter_for(validation_target(declared))

        def serialize(value: T) -> JsonBody[T]:
            validated = adapter.validate_python(value)
            return JsonBody(strip_unset(validated, adapter.dump_python(validated, mode="json")))

        return serialize

    if not TYPE_CHECKING:

        def __call__(self, *args, **kwargs):
            raise TypeError(
                "json_body is not called directly -- name the declared type in its subscript: "
                "json_body[T](value), e.g. json_body[Employee | EmployeeDict](model)"
            )


json_body: Final = _JsonBodyFactory()


def form_body(params: Sequence[Param[Any]]) -> FormBody:
    """Flatten ``params`` into a url-encoded form body.

    Args:
        params: The form parameters, each already carrying its declared type's adapter.

    Returns:
        A :class:`FormBody` holding wire-ready text fields.

    Raises:
        ValueError: If a parameter's value fails validation against its declared type."""
    return FormBody(to_fields(params))


def multipart_body(params: Sequence[Param[Any]], files: Mapping[str, Any]) -> MultipartBody:
    """Flatten ``params`` into multipart fields, to be sent alongside ``files``.

    Args:
        params: The non-file parameters, each already carrying its declared type's adapter.
        files: The file parts, keyed by field name; the value space is the transport's.

    Returns:
        A :class:`MultipartBody` holding wire-ready text fields and the files unchanged.

    Raises:
        ValueError: If a parameter's value fails validation against its declared type."""
    return MultipartBody(to_fields(params), dict(files))
