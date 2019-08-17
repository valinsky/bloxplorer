from unittest.mock import MagicMock

import pytest

from bloxplorer.constants import BITCOIN_API_BASE_URL
from bloxplorer.blocks import Blocks


Blocks.make_request = MagicMock()
blocks = Blocks(BITCOIN_API_BASE_URL)


def test_get_block():
    hash = '000000000000000000018899889c6c46714fc00f22670d23ace68e400a96a6d8'
    blocks.get(hash)
    blocks.make_request.assert_called_with('GET', f'block/{hash}')


def test_get_block_status():
    hash = '000000000000000000018899889c6c46714fc00f22670d23ace68e400a96a6d8'
    blocks.get_status(hash)
    blocks.make_request.assert_called_with('GET', f'block/{hash}/status')


def test_get_block_status_url():
    hash = '1234'
    blocks.get_status(hash)
    blocks.make_request.assert_called_with('GET', 'block/1234/status')


@pytest.mark.parametrize(
    'hash, start_index, expected_url', (
        ('1234', None, 'block/1234/txs'),
        ('1234', 10, 'block/1234/txs/10')
    ))
def test_get_block_txs(hash, start_index, expected_url):
    blocks.get_txs(hash, start_index)
    blocks.make_request.assert_called_with('GET', expected_url)


def test_get_block_txids():
    hash = '1234'
    blocks.get_txids(hash)
    blocks.make_request.assert_called_with('GET', f'block/{hash}/txids')


def test_get_block_height():
    height = 1234
    blocks.get_height(height)
    blocks.make_request.assert_called_with('GET', f'block-height/{height}')


@pytest.mark.parametrize(
    'start_height, expected_url', (
        (None, 'blocks'),
        (10, 'blocks/10')
    ))
def test_get_blocks(start_height, expected_url):
    blocks.get_blocks(start_height)
    blocks.make_request.assert_called_with('GET', expected_url)


def test_get_last_block_height():
    blocks.get_last_height()
    blocks.make_request.assert_called_with('GET', 'blocks/tip/height')


def test_get_last_block_hash():
    blocks.get_last_hash()
    blocks.make_request.assert_called_with('GET', 'blocks/tip/hash')
