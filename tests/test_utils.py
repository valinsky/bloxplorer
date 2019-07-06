from urllib.parse import urljoin

import pytest
from pytest_mock import mocker

from blockstreamesplora.constants import BITCOIN_API_BASE_URL
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

def test_get():
    pass