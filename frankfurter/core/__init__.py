"""Public surface of the SDK runtime.

Everything the generated layers (``api/``, ``models/``, ``errors/``, ``server/``, the two clients)
need from the runtime is re-exported here, so a generated module imports from one place --
``from <sdk>.core import ApiResult, RawClient, json_decoder`` -- instead of reaching into the
runtime's internal module layout. That indirection is the point: the modules behind this facade are
free to move without touching a single generated file.

A symbol earns a place here by one test: a generator may emit it, or a caller may need to name it.
Internal machinery the runtime only calls itself -- the adapter cache, the decoder implementation
classes, the sentinel stripper -- is deliberately absent, and remains reachable at its own module
path for the unit tests that target it.

Everything remains importable from its fully-qualified module path as well."""

from .auth import (
    AllSchemes,
    AnySchemes,
    AsyncAllSchemes,
    AsyncAnySchemes,
    AsyncAuthScheme,
    AsyncRefreshableTokenSource,
    AsyncTokenSource,
    AuthParams,
    AuthScheme,
    OAuthError,
    OAuthProviderError,
    OAuthToken,
    OAuthTokenRefreshable,
    RefreshableTokenSource,
    RevocableAuthScheme,
    TokenSource,
    client_secret_basic,
    client_secret_post,
    invalidate,
    is_configured,
    no_auth,
    oauth_error_response,
    resolve_auth,
)
from .auth.schemes import (
    ApiKeyCookieScheme,
    ApiKeyHeaderScheme,
    ApiKeyQueryScheme,
    AsyncAuthorizationCodeCredentials,
    AsyncAuthorizationCodeCredentialsDict,
    AsyncAuthorizationCodeCredentialsOrDict,
    AsyncAuthorizationCodePrompt,
    AsyncAuthorizationCodeTokenSource,
    AsyncClientCredentialsTokenSource,
    AsyncOAuth2RefreshableScheme,
    AsyncOAuth2Scheme,
    AsyncPasswordTokenSource,
    AuthorizationCodeCredentials,
    AuthorizationCodeCredentialsDict,
    AuthorizationCodeCredentialsOrDict,
    AuthorizationCodePrompt,
    AuthorizationCodeTokenSource,
    BasicAuthCredentials,
    BasicAuthCredentialsDict,
    BasicAuthCredentialsOrDict,
    BasicAuthScheme,
    BearerAuthScheme,
    ClientCredentials,
    ClientCredentialsDict,
    ClientCredentialsOrDict,
    ClientCredentialsTokenSource,
    OAuth2RefreshableScheme,
    OAuth2Scheme,
    PasswordCredentials,
    PasswordCredentialsDict,
    PasswordCredentialsOrDict,
    PasswordTokenSource,
    PkceMethod,
)
from .base_raw_response import BaseRawResponse, SecuredRawResponse
from .bodies import (
    FormBody,
    JsonBody,
    MultipartBody,
    RequestBody,
    form_body,
    json_body,
    multipart_body,
)
from .converters import (
    Date,
    RFC1123DateTime,
    RFC3339DateTime,
    UnixSecondsDateTime,
    open_enum_validator,
)
from .decoding import (
    ErrorMapper,
    ResponseDecoder,
    decode_json,
    decode_text,
    empty_response,
    json_decoder,
    raw_error_response,
    text_decoder,
)
from .exceptions import ApiError
from .httpx_transport import AsyncHttpxClient, HttpxClient
from .models import SdkBaseModel
from .optionality import UNSET, Optional, OptionalNullable, UnsetType
from .params import SerializationFormat, UrlTemplate, param
from .raw_client import (
    AsyncRawClient,
    RawClient,
    RawClientT,
)
from .request_options import RequestOptions, RequestOptionsDict, RequestOptionsOrDict
from .results import ApiResult, Failure, RawError, Success
from .servers import validate_one_of
from .transport import (
    AsyncHttpClient,
    HttpClient,
    HttpRequest,
    HttpResponse,
)

__all__ = [
    # Result and error types
    "ApiResult",
    "Success",
    "Failure",
    "RawError",
    "ApiError",
    # HTTP transport
    "HttpClient",
    "AsyncHttpClient",
    "HttpRequest",
    "HttpResponse",
    "HttpxClient",
    "AsyncHttpxClient",
    # Request parameters and bodies
    "param",
    "SerializationFormat",
    "UrlTemplate",
    "RequestBody",
    "JsonBody",
    "json_body",
    "FormBody",
    "form_body",
    "MultipartBody",
    "multipart_body",
    # Per-call request options
    "RequestOptions",
    "RequestOptionsDict",
    "RequestOptionsOrDict",
    # Authentication
    "AuthParams",
    "AuthScheme",
    "AsyncAuthScheme",
    "no_auth",
    "is_configured",
    "resolve_auth",
    "BasicAuthCredentials",
    "BasicAuthCredentialsDict",
    "BasicAuthCredentialsOrDict",
    "BasicAuthScheme",
    "BearerAuthScheme",
    "ApiKeyHeaderScheme",
    "ApiKeyQueryScheme",
    "ApiKeyCookieScheme",
    "AnySchemes",
    "AsyncAnySchemes",
    "AllSchemes",
    "AsyncAllSchemes",
    "RevocableAuthScheme",
    "invalidate",
    # Managed OAuth 2.0
    "OAuth2Scheme",
    "AsyncOAuth2Scheme",
    "OAuth2RefreshableScheme",
    "AsyncOAuth2RefreshableScheme",
    "TokenSource",
    "AsyncTokenSource",
    "RefreshableTokenSource",
    "AsyncRefreshableTokenSource",
    "client_secret_basic",
    "client_secret_post",
    "OAuthToken",
    "OAuthTokenRefreshable",
    "OAuthProviderError",
    "OAuthError",
    "oauth_error_response",
    # oauth2 / clientCredentials
    "ClientCredentials",
    "ClientCredentialsDict",
    "ClientCredentialsOrDict",
    "ClientCredentialsTokenSource",
    "AsyncClientCredentialsTokenSource",
    # oauth2 / password
    "PasswordCredentials",
    "PasswordCredentialsDict",
    "PasswordCredentialsOrDict",
    "PasswordTokenSource",
    "AsyncPasswordTokenSource",
    # oauth2 / authorizationCode
    "AuthorizationCodeCredentials",
    "AuthorizationCodeCredentialsDict",
    "AuthorizationCodeCredentialsOrDict",
    "AsyncAuthorizationCodeCredentials",
    "AsyncAuthorizationCodeCredentialsDict",
    "AsyncAuthorizationCodeCredentialsOrDict",
    "AuthorizationCodePrompt",
    "AsyncAuthorizationCodePrompt",
    "PkceMethod",
    "AuthorizationCodeTokenSource",
    "AsyncAuthorizationCodeTokenSource",
    # Response decoding and error mapping
    "ResponseDecoder",
    "ErrorMapper",
    "json_decoder",
    "text_decoder",
    "decode_json",
    "decode_text",
    "empty_response",
    "raw_error_response",
    # Model base and optionality
    "SdkBaseModel",
    "UNSET",
    "UnsetType",
    "Optional",
    "OptionalNullable",
    # Date/time and enum converters
    "Date",
    "RFC3339DateTime",
    "RFC1123DateTime",
    "UnixSecondsDateTime",
    "open_enum_validator",
    # Raw clients and the raw-response base
    "RawClient",
    "AsyncRawClient",
    "RawClientT",
    "BaseRawResponse",
    "SecuredRawResponse",
    # Server layer
    "validate_one_of",
]
