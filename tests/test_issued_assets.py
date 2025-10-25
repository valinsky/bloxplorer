import asyncio

from unittest.mock import AsyncMock, MagicMock

import pytest

from bloxplorer.constants import BITCOIN_API_BASE_URL, http
from bloxplorer.issued_assets import AsyncIssuedAssets, SyncIssuedAssets

SyncIssuedAssets.make_request = MagicMock()
sync_assets = SyncIssuedAssets(BITCOIN_API_BASE_URL)


def test_issued_asset_sync():
    asset_id = '1234'
    sync_assets.get(asset_id)
    sync_assets.make_request.assert_called_with(http.GET, 'asset/1234')


def test_issued_asset_txs_sync():
    asset_id = '1234'
    sync_assets.get_txs(asset_id)
    sync_assets.make_request.assert_called_with(http.GET, 'asset/1234/txs')


def test_issued_asset_mempool_sync():
    asset_id = '1234'
    sync_assets.get_mempool(asset_id)
    sync_assets.make_request.assert_called_with(http.GET, 'asset/1234/txs/mempool')


@pytest.mark.parametrize(
    'asset_id, last_seen, expected_url', (
        ('1234', None, 'asset/1234/txs/chain'),
        ('1234', 10, 'asset/1234/txs/chain/10')
    ))
def test_issued_asset_chain_sync(asset_id, last_seen, expected_url):
    sync_assets.get_chain(asset_id, last_seen)
    sync_assets.make_request.assert_called_with(http.GET, expected_url)


@pytest.mark.parametrize(
    'asset_id, decimal, expected_url', (
        ('1234', False, 'asset/1234/supply'),
        ('1234', True, 'asset/1234/supply/decimal')
    ))
def test_get_supply_sync(asset_id, decimal, expected_url):
    sync_assets.get_supply(asset_id, decimal)
    sync_assets.make_request.assert_called_with(http.GET, expected_url)


AsyncIssuedAssets.make_request = AsyncMock()
async_assets = AsyncIssuedAssets(BITCOIN_API_BASE_URL)


def test_issued_asset_async():
    asset_id = '1234'
    asyncio.run(async_assets.get(asset_id))
    async_assets.make_request.assert_called_with(http.GET, 'asset/1234')


def test_issued_asset_txs_async():
    asset_id = '1234'
    asyncio.run(async_assets.get_txs(asset_id))
    async_assets.make_request.assert_called_with(http.GET, 'asset/1234/txs')


def test_issued_asset_mempool_async():
    asset_id = '1234'
    asyncio.run(async_assets.get_mempool(asset_id))
    async_assets.make_request.assert_called_with(http.GET, 'asset/1234/txs/mempool')


@pytest.mark.parametrize(
    'asset_id, last_seen, expected_url', (
        ('1234', None, 'asset/1234/txs/chain'),
        ('1234', 10, 'asset/1234/txs/chain/10')
    ))
def test_issued_asset_chain_async(asset_id, last_seen, expected_url):
    asyncio.run(async_assets.get_chain(asset_id, last_seen))
    async_assets.make_request.assert_called_with(http.GET, expected_url)


@pytest.mark.parametrize(
    'asset_id, decimal, expected_url', (
        ('1234', False, 'asset/1234/supply'),
        ('1234', True, 'asset/1234/supply/decimal')
    ))
def test_get_supply_async(asset_id, decimal, expected_url):
    asyncio.run(async_assets.get_supply(asset_id, decimal))
    async_assets.make_request.assert_called_with(http.GET, expected_url)
