from unittest.mock import MagicMock

import pytest

from bloxplorer.constants import BITCOIN_API_BASE_URL, http
from bloxplorer.issued_assets import SyncIssuedAssets

SyncIssuedAssets.make_request = MagicMock()
sync_assets = SyncIssuedAssets(BITCOIN_API_BASE_URL)


def test_issued_asset():
    asset_id = '1234'
    sync_assets.get(asset_id)
    sync_assets.make_request.assert_called_with(http.GET, 'asset/1234')


def test_issued_asset_txs():
    asset_id = '1234'
    sync_assets.get_txs(asset_id)
    sync_assets.make_request.assert_called_with(http.GET, 'asset/1234/txs')


def test_issued_asset_mempool():
    asset_id = '1234'
    sync_assets.get_mempool(asset_id)
    sync_assets.make_request.assert_called_with(http.GET, 'asset/1234/txs/mempool')


@pytest.mark.parametrize(
    'asset_id, last_seen, expected_url', (
        ('1234', None, 'asset/1234/txs/chain'),
        ('1234', 10, 'asset/1234/txs/chain/10')
    ))
def test_issued_asset_chain(asset_id, last_seen, expected_url):
    sync_assets.get_chain(asset_id, last_seen)
    sync_assets.make_request.assert_called_with(http.GET, expected_url)


@pytest.mark.parametrize(
    'asset_id, decimal, expected_url', (
        ('1234', False, 'asset/1234/supply'),
        ('1234', True, 'asset/1234/supply/decimal')
    ))
def test_get_supply(asset_id, decimal, expected_url):
    sync_assets.get_supply(asset_id, decimal)
    sync_assets.make_request.assert_called_with(http.GET, expected_url)
