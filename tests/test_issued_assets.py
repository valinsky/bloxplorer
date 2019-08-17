from unittest.mock import MagicMock

import pytest

from bloxplorer.constants import BITCOIN_API_BASE_URL
from bloxplorer.issued_assets import IssuedAssets


IssuedAssets.make_request = MagicMock()
assets = IssuedAssets(BITCOIN_API_BASE_URL)


def test_issued_asset():
    asset_id = '1234'
    assets.get(asset_id)
    assets.make_request.assert_called_with('GET', 'asset/1234')


def test_issued_asset_txs():
    asset_id = '1234'
    assets.get_txs(asset_id)
    assets.make_request.assert_called_with('GET', 'asset/1234/txs')


def test_issued_asset_mempool():
    asset_id = '1234'
    assets.get_mempool(asset_id)
    assets.make_request.assert_called_with('GET', 'asset/1234/txs/mempool')


@pytest.mark.parametrize(
    'asset_id, last_seen, expected_url', (
        ('1234', None, 'asset/1234/txs/chain'),
        ('1234', 10, 'asset/1234/txs/chain/10')
    ))
def test_issued_asset_chain(asset_id, last_seen, expected_url):
    assets.get_chain(asset_id, last_seen)
    assets.make_request.assert_called_with('GET', expected_url)
