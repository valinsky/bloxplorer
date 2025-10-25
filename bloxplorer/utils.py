import asyncio
import inspect

from abc import ABC

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


class BaseRequest(ABC):
    __slots__ = ('_base_url', )

    def __init__(self, base_url):
        self._base_url = base_url

    @staticmethod
    async def _make_request(client, method, path, timeout, **kwargs):
        r"""
        Send a request to the Esplora API.

        :param client: `httpx.Client` or `httpx.AsyncClient` instance.
        :param method: The request method (get or post).
        :param path: String representing the URL resource path.
        :param timeout: The request timeout in seconds.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        try:
            response = client.request(method, path, timeout=timeout, **kwargs)
            if inspect.isawaitable(response):
                response = await response

        except httpx.TimeoutException:
            raise BlockstreamClientTimeout(
                message=REQUEST_TIMED_OUT_MESSAGE, resource_url=path, request_method=method)

        except httpx.NetworkError:
            raise BlockstreamClientNetworkError(
                message=NETWORK_ERROR_MESSAGE, resource_url=path, request_method=method)

        except httpx.RequestError as e:
            raise BlockstreamClientError(message=f'{e}', resource_url=path, request_method=method)

        return BaseRequest._handle_response(response)

    def make_request(self, method, path, timeout=DEFAULT_TIMEOUT, **kwargs):
        raise NotImplementedError('This method should be implemented in a subclass.')

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
    Class used to make sync requests.
    """
    def make_request(self, method, path, timeout=DEFAULT_TIMEOUT, **kwargs):
        with httpx.Client(base_url=self._base_url) as client:
            return asyncio.run(
                self._make_request(client, method, path, timeout, **kwargs)
            )


class AsyncRequest(BaseRequest):
    """
    Class used to make async requests.
    """

    async def make_request(self, method, path, timeout=DEFAULT_TIMEOUT, **kwargs):
        async with httpx.AsyncClient(base_url=self._base_url) as client:
            return await self._make_request(client, method, path, timeout=timeout, **kwargs)


class Response(BaseModel):
    """
    The `Response` model returned after an API call.
    """
    resource_url: str
    headers: dict
    method: str
    data: str | dict | list
