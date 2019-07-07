from unittest.mock import MagicMock
from urllib.parse import urljoin

import pytest
import requests

from blockstreamesplora.constants import BITCOIN_API_BASE_URL, DEFAULT_TIMEOUT
from blockstreamesplora.utils import Request


request = Request()


def test_default_base_url():
    assert request.BASE_API_URL == BITCOIN_API_BASE_URL


def test_get_from_path(mocker):
    mock_get = mocker.patch('blockstreamesplora.utils.Request._get')
    url_path = 'some/path'
    timeout = 10
    headers = {'Content-Type': 'application/json'}

    request.get_from_path(url_path, timeout=timeout, headers=headers)

    url = urljoin(BITCOIN_API_BASE_URL, url_path)
    mock_get.assert_called_with(url, timeout=timeout, headers=headers)


def test__get(mocker):
    url = 'www.thecakeisalie.com/api'
    mock_requests = mocker.patch('blockstreamesplora.utils.requests.get')
    mock_requests.return_value = MagicMock(json={'response': 'success'}, status_code=200)

    response = request._get(url)

    mock_requests.assert_called_with(url, headers=None, timeout=DEFAULT_TIMEOUT)
    assert response.json == {'response': 'success'}
    assert response.status_code == 200


def test__get_error(mocker):
    url = 'www.thecakeisalie.com/api'
    mock_requests = mocker.patch('blockstreamesplora.utils.requests.get')
    mock_requests.side_effect = requests.exceptions.Timeout

    with pytest.raises(requests.exceptions.Timeout):
        request._get(url)
