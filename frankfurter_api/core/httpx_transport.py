"""httpx-backed transports -- the default implementations of the two transport protocols.

The sync and async adapters live together because they are peers differing only in ``await``, the
same reason :class:`RawClient` and :class:`AsyncRawClient` share a module. Everything httpx-specific
is confined here: swapping HTTP libraries means writing one more module like this one, not touching
anything else."""

from __future__ import annotations

import ssl
from collections.abc import Mapping
from typing import Any

import httpx

from .bodies import FormBody, JsonBody, MultipartBody
from .transport import (
    AsyncHttpClient,
    HttpClient,
    HttpRequest,
    HttpResponse,
)

_DEFAULT_TIMEOUT = 30.0


def _multipart_parts(
    fields: Mapping[str, str | list[str]],
    files: Mapping[str, Any],
) -> list[tuple[str, Any]]:
    """Render both halves of a multipart body as one sequence of explicit parts.

    The text fields go through httpx's *file* spelling -- ``(None, text)``, a part with no
    filename -- rather than through ``data=``, because httpx chooses the encoding on the
    **truthiness** of ``files``: an operation declaring ``multipart/form-data`` with no binary part
    would otherwise be sent as ``application/x-www-form-urlencoded``. The rendered bytes are
    identical either way, repeated keys and name escaping included, so the invariant costs nothing.

    A sequence rather than a mapping, because a field may repeat: one part per value.

    Args:
        fields: The flattened text fields, each one text or the list of texts its key collected.
        files: The file parts, keyed by field name.

    Returns:
        ``(name, part)`` pairs in httpx's ``files=`` shape -- one entry per value, so a repeated
        key survives."""
    parts: list[tuple[str, Any]] = [
        (name, (None, text))
        for name, value in fields.items()
        for text in (value if isinstance(value, list) else [value])
    ]
    parts.extend(files.items())
    return parts


def _body_kwargs(request: HttpRequest) -> dict[str, Any]:
    """Map the request's body -- and the headers that describe it -- onto httpx's keywords.

    This ``match`` is the only place the body union is interpreted, and it is exhaustive by
    construction: adding a body shape without handling it here is a type error.

    The headers are returned here rather than passed separately because httpx derives the media type
    from *which* keyword it receives, and one shape cannot be handed to the keyword that would
    derive it -- so that arm carries the media type itself, underneath the request's own headers,
    which still win exactly as they do over a media type httpx derived.

    Args:
        request: The request whose body and headers are being mapped.

    Returns:
        The httpx keyword arguments carrying this body, ``headers`` among them."""
    match request.body:
        case None:
            return {"headers": request.headers}
        case JsonBody(None):
            # ``json=None`` is indistinguishable to httpx from no ``json`` argument at all, so the
            # body would vanish rather than going out as the four bytes the caller asked for.
            # ``content=`` is the only keyword that will carry them, and it declares no media type.
            return {
                "headers": {"content-type": "application/json", **request.headers},
                "content": b"null",
            }
        case JsonBody(value):
            return {"headers": request.headers, "json": value}
        case FormBody(fields):
            return {"headers": request.headers, "data": fields}
        case MultipartBody(fields, files):
            return {"headers": request.headers, "files": _multipart_parts(fields, files)}


def _timeout_kwargs(request: HttpRequest) -> dict[str, Any]:
    """Map a per-request timeout onto httpx's keyword, or contribute nothing.

    Omitting is deliberate rather than passing ``timeout=None``: to httpx that means *no timeout at
    all*, not *use the client's own*, so an absent override must not reach the call.

    Args:
        request: The request whose ``timeout`` is being mapped.

    Returns:
        ``{"timeout": ...}`` when the request set one, otherwise an empty mapping."""
    return {} if request.timeout is None else {"timeout": httpx.Timeout(request.timeout)}


class HttpxClient(HttpClient):
    """Sync transport backed by httpx.

    Uses connection pooling via a single ``httpx.Client``, and returns buffered responses.

    Requests honour the standard proxy and TLS environment variables -- ``HTTP_PROXY`` /
    ``HTTPS_PROXY`` / ``ALL_PROXY`` / ``NO_PROXY`` (consulted only when ``proxy_url`` is unset) and
    ``SSL_CERT_FILE`` / ``SSL_CERT_DIR`` (the trust store). That is the underlying library's default
    rather than a decision made here, and it is stated because it is request behaviour the
    environment can change; a caller needing it off supplies a transport of their own.

    ``verify`` takes an ``ssl.SSLContext`` as well as a bool: a private CA bundle or a client
    certificate is configured by building one (``ssl.create_default_context(cafile=...)``), which is
    the one spelling the pinned library still supports for either."""

    def __init__(
        self,
        *,
        timeout: float = _DEFAULT_TIMEOUT,
        proxy_url: str | None = None,
        verify: ssl.SSLContext | bool = True,
    ) -> None:
        self._client = httpx.Client(
            proxy=proxy_url,
            timeout=httpx.Timeout(timeout),
            verify=verify,
        )
        self._closed = False

    def send(self, request: HttpRequest) -> HttpResponse:
        response = self._client.request(
            method=request.method,
            url=request.url,
            **_timeout_kwargs(request),
            **_body_kwargs(request),
        )

        return HttpResponse(
            status_code=response.status_code,
            headers=dict(response.headers),
            content=response.content,
            request=request,
        )

    def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        self._client.close()


class AsyncHttpxClient(AsyncHttpClient):
    """Async transport backed by httpx.

    Uses connection pooling via a single ``httpx.AsyncClient``, and returns buffered responses.

    Requests honour the standard proxy and TLS environment variables -- ``HTTP_PROXY`` /
    ``HTTPS_PROXY`` / ``ALL_PROXY`` / ``NO_PROXY`` (consulted only when ``proxy_url`` is unset) and
    ``SSL_CERT_FILE`` / ``SSL_CERT_DIR`` (the trust store). That is the underlying library's default
    rather than a decision made here, and it is stated because it is request behaviour the
    environment can change; a caller needing it off supplies a transport of their own.

    ``verify`` takes an ``ssl.SSLContext`` as well as a bool: a private CA bundle or a client
    certificate is configured by building one (``ssl.create_default_context(cafile=...)``), which is
    the one spelling the pinned library still supports for either."""

    def __init__(
        self,
        *,
        timeout: float = _DEFAULT_TIMEOUT,
        proxy_url: str | None = None,
        verify: ssl.SSLContext | bool = True,
    ) -> None:
        self._client = httpx.AsyncClient(
            proxy=proxy_url,
            timeout=httpx.Timeout(timeout),
            verify=verify,
        )
        self._closed = False

    async def send(self, request: HttpRequest) -> HttpResponse:
        response = await self._client.request(
            method=request.method,
            url=request.url,
            **_timeout_kwargs(request),
            **_body_kwargs(request),
        )

        return HttpResponse(
            status_code=response.status_code,
            headers=dict(response.headers),
            content=response.content,
            request=request,
        )

    async def aclose(self) -> None:
        if self._closed:
            return
        self._closed = True
        await self._client.aclose()
