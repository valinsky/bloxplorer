from urllib.parse import urljoin

import requests

from bloxplorer.constants import CONTENT_TYPE_JSON, CONTENT_TYPE_TEXT, DEFAULT_TIMEOUT
from bloxplorer.exceptions import (
    BlockstreamApiError, BlockstreamClientError, BlockstreamClientNetworkError,
    BlockstreamClientTimeout
)


class Request:
    """
    Parent class used to send requests to, and handle responses from, the Blockstream Esplora API.
    """
    def __init__(self, base_url):
        self.base_url = base_url

    def make_request(self, method, path, **kwargs):
        r"""
        Send an http request to the Esplora endpoint specified by `path`.

        :param method: The request method (get or post).
        :param path: String representing the URL resource path.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        url = self._prepare_resource_url(path)
        return self._request(method, url, **kwargs)

    def _request(self, method, url, timeout=DEFAULT_TIMEOUT, **kwargs):
        r"""
        Helper method that sends an http request and handles the response.

        :param method: The request method (get or post).
        :param url: String representing the resource URL.
        :param timeout: (Optional) The request timeout. Default is 5 seconds.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        try:
            response = requests.request(method, url, timeout=timeout, **kwargs)

        except requests.exceptions.Timeout:
            raise BlockstreamClientTimeout(
                message='Request timed out.', resource_url=url, request_method=method)

        except requests.exceptions.ConnectionError:
            raise BlockstreamClientNetworkError(
                message='Network error.', resource_url=url, request_method=method)

        except requests.exceptions.RequestException as e:
            raise BlockstreamClientError(message=str(e), resource_url=url, request_method=method)

        return self._handle_response(response)

    def _prepare_resource_url(self, path):
        """
        Helper method that construct the resource URL from `base_url` and a specified `path`

        :param path: String representing the URL resource path.

        :return: String representing the full resource URL.
        """
        return urljoin(self.base_url, path)

    @staticmethod
    def _handle_response(response):
        """
        Helper static method that takes a `Requests` response and returns a processed `Response`.

        :param response: `Requests` object.

        :return: :class: `Response` object.
        """
        method = response.request.method
        content_type = response.headers.get('content-type')
        data = None

        if content_type == CONTENT_TYPE_JSON:
            data = response.json()
        elif content_type == CONTENT_TYPE_TEXT:
            data = response.text

        if response.status_code == requests.codes.ok:
            return Response(response, data)

        if response.status_code == requests.codes.bad_request:
            raise BlockstreamApiError(
                message=data, resource_url=response.url, request_method=method,
                status_code=response.status_code)

        if response.status_code == requests.codes.not_found:
            raise BlockstreamApiError(
                message='Invalid API resource.', resource_url=response.url, request_method=method,
                status_code=response.status_code)

        raise BlockstreamApiError(
            message='An unknown error occured while processing your request.',
            resource_url=response.url, request_method=method, status_code=response.status_code)


class Response:
    """
    Class used to create the `Response` object returned after an API call.
    """

    __slots__ = ['resource_url', 'headers', 'method', 'data']

    def __init__(self, response, data):
        self.resource_url = response.url
        self.headers = response.headers
        self.method = response.request.method
        self.data = data
