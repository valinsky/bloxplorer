import json
from unittest.mock import MagicMock
from urllib.parse import urljoin

import pytest
import requests

from bloxplorer.constants import DEFAULT_TIMEOUT, CONTENT_TYPE_JSON, CONTENT_TYPE_TEXT
from bloxplorer.exceptions import (
    BlockstreamApiError, BlockstreamClientError, BlockstreamClientTimeout,
    BlockstreamClientNetworkError
)
from bloxplorer.utils import Request


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


def test__request(mocker):
    method = 'GET'
    url = 'www.thecakeisalie.com/api/42'
    mock_request = mocker.patch('bloxplorer.utils.requests.request')
    mock_response = MagicMock()
    mock_request.return_value = mock_response
    mock_handle_response = mocker.patch('bloxplorer.utils.Request._handle_response')

    request = Request('www.thecakeisalie.com/api')
    request._request(method, url)

    mock_request.assert_called_with(method, url, timeout=DEFAULT_TIMEOUT)
    mock_handle_response.assert_called_with(mock_response)


def test__request_parameters(mocker):
    method = 'GET'
    url = 'www.thecakeisalie.com/api/42'
    timeout = 10
    headers = {
        'blah': 'blah'
    }
    kwargzilla = 'yeet'

    mock_request = mocker.patch('bloxplorer.utils.requests.request')
    mock_response = MagicMock()
    mock_request.return_value = mock_response
    mock_handle_response = mocker.patch('bloxplorer.utils.Request._handle_response')

    request = Request('www.thecakeisalie.com/api')
    request._request(method, url, timeout=timeout, headers=headers, kwargzilla=kwargzilla)

    mock_request.assert_called_with(method, url, timeout=timeout, headers=headers, kwargzilla=kwargzilla)
    mock_handle_response.assert_called_with(mock_response)


@pytest.mark.parametrize(
    'exception, raised_exception', (
        (requests.exceptions.Timeout, BlockstreamClientTimeout),
        (requests.exceptions.ConnectionError, BlockstreamClientNetworkError),
        (requests.exceptions.RequestException, BlockstreamClientError),
    )
)
def test__request_raises(mocker, exception, raised_exception):
    url = 'www.thecakeisalie.com/api/42'
    mock_request = mocker.patch('bloxplorer.utils.requests.request')
    mock_request.side_effect = exception

    request = Request('www.thecakeisalie.com/api')

    with pytest.raises(raised_exception):
        request._request('GET', url)


def test__prepare_resource_url():
    base_url = 'www.thecakeisalie.com/api/'
    path = 'answer/is/42'
    expected = 'www.thecakeisalie.com/api/answer/is/42'

    request = Request(base_url)

    assert request._prepare_resource_url(path) == expected


def test_make_request(mocker):
    method = 'GET'
    base_url = 'www.thecakeisalie.com/api/'
    path = 'answer/is/42'
    url = urljoin(base_url, path)
    kwargs = {'nitty': 'gritty'}
    mock__request = mocker.patch('bloxplorer.utils.Request._request')

    request = Request(base_url)
    request.make_request(method, path, **kwargs)

    mock__request.assert_called_with(method, url, **kwargs)


def test__handle_response_json(mocker):
    url = 'www.thecakeisalie.com/api/answer/is/42'
    headers = {'content-type': CONTENT_TYPE_JSON}
    data = '{"block": "1234"}'
    method = 'GET'
    response = MockResponse(
        data=data, headers=headers, status_code=requests.codes.ok, url=url, method=method
    )

    response = Request._handle_response(response)

    assert response.resource_url == url
    assert response.headers == headers
    assert response.method == method
    assert isinstance(response.data, dict)
    assert response.data == json.loads(data)


def test__handle_response_text(mocker):
    url = 'www.thecakeisalie.com/api/answer/is/42'
    headers = {'content-type': CONTENT_TYPE_TEXT}
    data = '1234'
    method = 'GET'
    response = MockResponse(
        data=data, headers=headers, status_code=requests.codes.ok, url=url, method=method
    )

    response = Request._handle_response(response)

    assert response.resource_url == url
    assert response.headers == headers
    assert response.method == method
    assert isinstance(response.data, str)
    assert response.data == data


@pytest.mark.parametrize(
    'status_code, exception', (
        (requests.codes.bad_request, BlockstreamApiError),
        (requests.codes.not_found, BlockstreamApiError),
        (requests.codes.im_a_teapot, BlockstreamApiError),
    )
)
def test__handle_response_raises(mocker, status_code, exception):
    url = 'www.thecakeisalie.com/api/answer/is/42'
    headers = {'content-type': CONTENT_TYPE_TEXT}
    data = None
    method = 'GET'
    response = MockResponse(
        data=data, headers=headers, status_code=status_code, url=url, method=method
    )

    with pytest.raises(exception):
        response = Request._handle_response(response)

        assert response.resource_url == url
        assert response.headers == headers
        assert response.method == method
        assert isinstance(response.data, str)
        assert response.data == data
