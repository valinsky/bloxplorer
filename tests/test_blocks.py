from unittest.mock import MagicMock

import pytest

from bloxplorer.blocks import SyncBlocks
from bloxplorer.constants import BITCOIN_API_BASE_URL, http

SyncBlocks.make_request = MagicMock()
sync_blocks = SyncBlocks(BITCOIN_API_BASE_URL)


def test_get_block():
    hash = '000000000000000000018899889c6c46714fc00f22670d23ace68e400a96a6d8'
    sync_blocks.get(hash)
    sync_blocks.make_request.assert_called_with(http.GET, f'block/{hash}')


def test_get_block_status():
    hash = '000000000000000000018899889c6c46714fc00f22670d23ace68e400a96a6d8'
    sync_blocks.get_status(hash)
    sync_blocks.make_request.assert_called_with(http.GET, f'block/{hash}/status')


def test_get_block_status_url():
    hash = '1234'
    sync_blocks.get_status(hash)
    sync_blocks.make_request.assert_called_with(http.GET, 'block/1234/status')


@pytest.mark.parametrize(
    'hash, start_index, expected_url', (
        ('1234', None, 'block/1234/txs'),
        ('1234', 10, 'block/1234/txs/10')
    ))
def test_get_block_txs(hash, start_index, expected_url):
    sync_blocks.get_txs(hash, start_index)
    sync_blocks.make_request.assert_called_with(http.GET, expected_url)


@pytest.mark.parametrize(
    'hash, index, expected_url', (
        ('1234', None, 'block/1234/txids'),
        ('1234', 10, 'block/1234/txid/10')
    ))
def test_get_block_txids(hash, index, expected_url):
    hash = '1234'
    sync_blocks.get_txids(hash, index)
    sync_blocks.make_request.assert_called_with(http.GET, expected_url)


def test_get_block_height():
    height = 1234
    sync_blocks.get_height(height)
    sync_blocks.make_request.assert_called_with(http.GET, f'block-height/{height}')


@pytest.mark.parametrize(
    'start_height, expected_url', (
        (None, 'blocks'),
        (10, 'blocks/10')
    ))
def test_get_blocks(start_height, expected_url):
    sync_blocks.get_blocks(start_height)
    sync_blocks.make_request.assert_called_with(http.GET, expected_url)


def test_get_last_block_height():
    sync_blocks.get_last_height()
    sync_blocks.make_request.assert_called_with(http.GET, 'blocks/tip/height')


def test_get_last_block_hash():
    sync_blocks.get_last_hash()
    sync_blocks.make_request.assert_called_with(http.GET, 'blocks/tip/hash')
