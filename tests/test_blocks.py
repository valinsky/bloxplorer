import asyncio

from unittest.mock import AsyncMock, MagicMock

import pytest

from bloxplorer.blocks import AsyncBlocks, SyncBlocks
from bloxplorer.constants import BITCOIN_API_BASE_URL, http

SyncBlocks.make_request = MagicMock()
sync_blocks = SyncBlocks(BITCOIN_API_BASE_URL)


def test_get_block_sync():
    hash = '000000000000000000018899889c6c46714fc00f22670d23ace68e400a96a6d8'
    sync_blocks.get(hash)
    sync_blocks.make_request.assert_called_with(http.GET, f'block/{hash}')


def test_get_block_status_sync():
    hash = '000000000000000000018899889c6c46714fc00f22670d23ace68e400a96a6d8'
    sync_blocks.get_status(hash)
    sync_blocks.make_request.assert_called_with(http.GET, f'block/{hash}/status')


def test_get_block_status_url_sync():
    hash = '1234'
    sync_blocks.get_status(hash)
    sync_blocks.make_request.assert_called_with(http.GET, 'block/1234/status')


@pytest.mark.parametrize(
    'hash, start_index, expected_url', (
        ('1234', None, 'block/1234/txs'),
        ('1234', 10, 'block/1234/txs/10')
    ))
def test_get_block_txs_sync(hash, start_index, expected_url):
    sync_blocks.get_txs(hash, start_index)
    sync_blocks.make_request.assert_called_with(http.GET, expected_url)


@pytest.mark.parametrize(
    'hash, index, expected_url', (
        ('1234', None, 'block/1234/txids'),
        ('1234', 10, 'block/1234/txid/10')
    ))
def test_get_block_txids_sync(hash, index, expected_url):
    hash = '1234'
    sync_blocks.get_txids(hash, index)
    sync_blocks.make_request.assert_called_with(http.GET, expected_url)


def test_get_block_height_sync():
    height = 1234
    sync_blocks.get_height(height)
    sync_blocks.make_request.assert_called_with(http.GET, f'block-height/{height}')


@pytest.mark.parametrize(
    'start_height, expected_url', (
        (None, 'blocks'),
        (10, 'blocks/10')
    ))
def test_get_blocks_sync(start_height, expected_url):
    sync_blocks.get_blocks(start_height)
    sync_blocks.make_request.assert_called_with(http.GET, expected_url)


def test_get_last_block_height_sync():
    sync_blocks.get_last_height()
    sync_blocks.make_request.assert_called_with(http.GET, 'blocks/tip/height')


def test_get_last_block_hash_sync():
    sync_blocks.get_last_hash()
    sync_blocks.make_request.assert_called_with(http.GET, 'blocks/tip/hash')


AsyncBlocks.make_request = AsyncMock()
async_blocks = AsyncBlocks(BITCOIN_API_BASE_URL)


def test_get_block_async():
    hash = '000000000000000000018899889c6c46714fc00f22670d23ace68e400a96a6d8'
    asyncio.run(async_blocks.get(hash))
    async_blocks.make_request.assert_called_with(http.GET, f'block/{hash}')


def test_get_block_status_async():
    hash = '000000000000000000018899889c6c46714fc00f22670d23ace68e400a96a6d8'
    asyncio.run(async_blocks.get_status(hash))
    async_blocks.make_request.assert_called_with(http.GET, f'block/{hash}/status')


def test_get_block_status_url_async():
    hash = '1234'
    asyncio.run(async_blocks.get_status(hash))
    async_blocks.make_request.assert_called_with(http.GET, 'block/1234/status')


@pytest.mark.parametrize(
    'hash, start_index, expected_url', (
        ('1234', None, 'block/1234/txs'),
        ('1234', 10, 'block/1234/txs/10')
    ))
def test_get_block_txs_async(hash, start_index, expected_url):
    asyncio.run(async_blocks.get_txs(hash, start_index))
    async_blocks.make_request.assert_called_with(http.GET, expected_url)


@pytest.mark.parametrize(
    'hash, index, expected_url', (
        ('1234', None, 'block/1234/txids'),
        ('1234', 10, 'block/1234/txid/10')
    ))
def test_get_block_txids_async(hash, index, expected_url):
    hash = '1234'
    asyncio.run(async_blocks.get_txids(hash, index))
    async_blocks.make_request.assert_called_with(http.GET, expected_url)


def test_get_block_height_async():
    height = 1234
    asyncio.run(async_blocks.get_height(height))
    async_blocks.make_request.assert_called_with(http.GET, f'block-height/{height}')


@pytest.mark.parametrize(
    'start_height, expected_url', (
        (None, 'blocks'),
        (10, 'blocks/10')
    ))
def test_get_blocks_async(start_height, expected_url):
    asyncio.run(async_blocks.get_blocks(start_height))
    async_blocks.make_request.assert_called_with(http.GET, expected_url)


def test_get_last_block_height_async():
    asyncio.run(async_blocks.get_last_height())
    async_blocks.make_request.assert_called_with(http.GET, 'blocks/tip/height')


def test_get_last_block_hash_async():
    asyncio.run(async_blocks.get_last_hash())
    async_blocks.make_request.assert_called_with(http.GET, 'blocks/tip/hash')
