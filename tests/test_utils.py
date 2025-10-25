import asyncio
import json

from unittest.mock import AsyncMock, MagicMock

import httpx
import pytest

from bloxplorer.constants import CONTENT_TYPE_JSON, CONTENT_TYPE_TEXT, DEFAULT_TIMEOUT, http
from bloxplorer.exceptions import (
    BlockstreamApiError, BlockstreamClientError, BlockstreamClientNetworkError,
    BlockstreamClientTimeout
)
from bloxplorer.utils import AsyncRequest, SyncRequest

BASE_URL_TEST = 'http://thecakeisalie.com/api/'


class MockResponse:
    def __init__(self, data, headers, status_code, url, method):
        self.data = data
        self.headers = headers
        self.status_code = status_code
        self.url = url
        self.request = MagicMock(method=method)

    def json(self):
        return json.loads(self.data)

    @property
    def text(self):
        return str(self.data)


def test_make_request(mocker):
    method = http.GET
    url = f'{BASE_URL_TEST}/42'
    mock_request = mocker.patch('bloxplorer.utils.httpx.Client.request')
    mock_response = MagicMock()
    mock_request.return_value = mock_response
    mock_handle_response = mocker.patch('bloxplorer.utils.BaseRequest._handle_response')

    request = SyncRequest(BASE_URL_TEST)
    request.make_request(method, url)

    mock_request.assert_called_with(method, url, timeout=DEFAULT_TIMEOUT)
    mock_handle_response.assert_called_with(mock_response)


def test_make_request_parameters(mocker):
    method = http.GET
    url = f'{BASE_URL_TEST}/42'
    timeout = 10
    headers = {
        'content-type': CONTENT_TYPE_JSON,
        'blah': 'blah'
    }
    kwargzilla = 'yeet'

    mock_request = mocker.patch('bloxplorer.utils.httpx.Client.request')
    mock_response = MagicMock()
    mock_request.return_value = mock_response
    mock_handle_response = mocker.patch('bloxplorer.utils.BaseRequest._handle_response')

    request = SyncRequest(BASE_URL_TEST)
    request.make_request(method, url, timeout=timeout, headers=headers, kwargzilla=kwargzilla)

    mock_request.assert_called_with(method, url, timeout=timeout, headers=headers, kwargzilla=kwargzilla)
    mock_handle_response.assert_called_with(mock_response)


@pytest.mark.parametrize(
    'exception, raised_exception', (
        (httpx.TimeoutException('Test timeout error'), BlockstreamClientTimeout),
        (httpx.NetworkError('Test network error'), BlockstreamClientNetworkError),
        (httpx.RequestError('Test request error'), BlockstreamClientError),
    )
)
def test_make_request_raises(mocker, exception, raised_exception):
    url = f'{BASE_URL_TEST}/42'
    mock_request = mocker.patch('bloxplorer.utils.httpx.Client.request')
    mock_request.side_effect = exception

    request = SyncRequest(BASE_URL_TEST)

    with pytest.raises(raised_exception):
        request.make_request(http.GET, url)


def test_make_request(mocker):
    method = http.GET
    path = 'answer/is/42'
    kwargs = {'nitty': 'gritty'}
    mock__request = mocker.patch('bloxplorer.utils.SyncRequest.make_request')

    request = SyncRequest(BASE_URL_TEST)
    request.make_request(method, path, **kwargs)

    mock__request.assert_called_with(method, path, **kwargs)


def test__handle_response_json(mocker):
    url = f'{BASE_URL_TEST}is/42'
    headers = {'content-type': CONTENT_TYPE_JSON}
    data = '{"block": "1234"}'
    method = http.GET
    response = MockResponse(
        data=data, headers=headers, status_code=httpx.codes.ok, url=url, method=method
    )

    response = SyncRequest._handle_response(response)

    assert response.resource_url == url
    assert response.headers == headers
    assert response.method == method
    assert isinstance(response.data, dict)
    assert response.data == json.loads(data)


def test__handle_response_text(mocker):
    url = f'{BASE_URL_TEST}answer/is/42'
    headers = {'content-type': CONTENT_TYPE_TEXT}
    data = '1234'
    method = http.GET
    response = MockResponse(
        data=data, headers=headers, status_code=httpx.codes.ok, url=url, method=method
    )

    response = SyncRequest._handle_response(response)

    assert response.resource_url == url
    assert response.headers == headers
    assert response.method == method
    assert isinstance(response.data, str)
    assert response.data == data


@pytest.mark.parametrize(
    'status_code, exception', (
        (httpx.codes.bad_request, BlockstreamApiError),
        (httpx.codes.not_found, BlockstreamApiError),
        (httpx.codes.im_a_teapot, BlockstreamApiError),
    )
)
def test__handle_response_raises(mocker, status_code, exception):
    url = f'{BASE_URL_TEST}answer/is/42'
    headers = {'content-type': CONTENT_TYPE_TEXT}
    data = None
    method = http.GET
    response = MockResponse(
        data=data, headers=headers, status_code=status_code, url=url, method=method
    )

    with pytest.raises(exception):
        response = SyncRequest._handle_response(response)

        assert response.resource_url == url
        assert response.headers == headers
        assert response.method == method
        assert isinstance(response.data, str)
        assert response.data == data


def test_make_request_async(mocker):
    method = http.GET
    url = f'{BASE_URL_TEST}/42'
    mock_request = mocker.patch('bloxplorer.utils.httpx.AsyncClient.request')
    mock_response = AsyncMock()
    mock_request.return_value = mock_response
    mock_handle_response = mocker.patch('bloxplorer.utils.BaseRequest._handle_response')

    request = AsyncRequest(BASE_URL_TEST)
    asyncio.run(request.make_request(method, url))

    mock_request.assert_called_with(method, url, timeout=DEFAULT_TIMEOUT)
    mock_handle_response.assert_called_with(mock_response)
