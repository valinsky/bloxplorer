import httpx

from pydantic import BaseModel

from bloxplorer.constants import (
    CONTENT_TYPE_JSON, CONTENT_TYPE_TEXT, DEFAULT_TIMEOUT, INVALID_API_RESOURCE_MESSAGE,
    NETWORK_ERROR_MESSAGE, REQUEST_TIMED_OUT_MESSAGE, UNKNOWN_ERROR_MESSAGE
)
from bloxplorer.exceptions import (
    BlockstreamApiError, BlockstreamClientError, BlockstreamClientNetworkError,
    BlockstreamClientTimeout
)


class BaseRequest:
    __slots__ = ('_base_url', )

    def __init__(self, base_url):
        self._base_url = base_url

    @staticmethod
    def _handle_response(response):
        """
        Helper static method that takes a `Requests` response and returns a processed `Response`.

        :param response: `Requests` object.

        :return: :class: `Response` object.
        """
        method = response.request.method
        resource_url = f'{response.url}'
        content_type = response.headers.get('content-type')
        data = None

        if content_type == CONTENT_TYPE_JSON:
            data = response.json()
        elif content_type == CONTENT_TYPE_TEXT:
            data = response.text

        if response.status_code == httpx.codes.ok:
            return Response(
                resource_url=resource_url,
                headers=dict(response.headers),
                method=method,
                data=data,
            )

        if response.status_code == httpx.codes.bad_request:
            raise BlockstreamApiError(
                message=data, resource_url=resource_url, request_method=method,
                status_code=response.status_code)

        if response.status_code == httpx.codes.not_found:
            raise BlockstreamApiError(
                message=INVALID_API_RESOURCE_MESSAGE, resource_url=resource_url, request_method=method,
                status_code=response.status_code)

        raise BlockstreamApiError(
            message=UNKNOWN_ERROR_MESSAGE,
            resource_url=resource_url, request_method=method, status_code=response.status_code)


class SyncRequest(BaseRequest):
    """
    Parent class used to send sync requests to, and handle responses from, the Blockstream Esplora API.
    """

    def make_request(self, method, path, timeout=DEFAULT_TIMEOUT, **kwargs):
        r"""
        Send an http sync request to the Esplora endpoint specified by `path`.

        :param method: The request method (get or post).
        :param path: String representing the URL resource path.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        try:
            with httpx.Client(base_url=self._base_url) as client:
                response = client.request(method, path, timeout=timeout, **kwargs)

        except httpx.TimeoutException:
            raise BlockstreamClientTimeout(
                message=REQUEST_TIMED_OUT_MESSAGE, resource_url=path, request_method=method)

        except httpx.NetworkError:
            raise BlockstreamClientNetworkError(
                message=NETWORK_ERROR_MESSAGE, resource_url=path, request_method=method)

        except httpx.RequestError as e:
            raise BlockstreamClientError(message=f'{e}', resource_url=path, request_method=method)

        return self._handle_response(response)


class AsyncRequest(BaseRequest):
    """
    Parent class used to send async requests to, and handle responses from, the Blockstream Esplora API.
    """

    async def make_request(self, method, path, timeout=DEFAULT_TIMEOUT, **kwargs):
        r"""
        Send an http async request to the Esplora endpoint specified by `path`.

        :param method: The request method (get or post).
        :param path: String representing the URL resource path.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        try:
            async with httpx.AsyncClient(base_url=self._base_url) as client:
                response = await client.request(method, path, timeout=timeout, **kwargs)

        # TODO: add full resource_url
        except httpx.TimeoutException:
            raise BlockstreamClientTimeout(
                message=REQUEST_TIMED_OUT_MESSAGE, resource_url=path, request_method=method)

        except httpx.NetworkError:
            raise BlockstreamClientNetworkError(
                message=NETWORK_ERROR_MESSAGE, resource_url=path, request_method=method)

        except httpx.RequestError as e:
            raise BlockstreamClientError(message=f'{e}', resource_url=path, request_method=method)

        return self._handle_response(response)


class Response(BaseModel):
    """
    The `Response` model returned after an API call.
    """
    resource_url: str
    headers: dict
    method: str
    data: str | dict
