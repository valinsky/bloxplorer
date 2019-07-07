from unittest.mock import MagicMock

import pytest

from blockstreamesplora.blocks import Blocks


Blocks.get_from_path = MagicMock()
blocks = Blocks()


def test_get_block():
    hash = '1234'
    blocks.get_block(hash)
    blocks.get_from_path.assert_called_with('block/1234')


def test_get_block_status():
    hash = '1234'
    blocks.get_block_status(hash)
    blocks.get_from_path.assert_called_with('block/1234/status')


@pytest.mark.parametrize(
    'hash, start_index, expected_url', (
        ('1234', None, 'block/1234/txs'),
        ('1234', 10, 'block/1234/txs/10')
    ))
def test_get_block_txs(hash, start_index, expected_url):
    blocks.get_block_txs(hash, start_index)
    blocks.get_from_path.assert_called_with(expected_url)


def test_get_block_txids():
    hash = '1234'
    blocks.get_block_txids(hash)
    blocks.get_from_path.assert_called_with(f'block/{hash}/txids')


def test_get_block_height():
    height = 1234
    blocks.get_block_height(height)
    blocks.get_from_path.assert_called_with(f'block-height/{height}')


@pytest.mark.parametrize(
    'start_height, expected_url', (
        (None, 'blocks'),
        (10, 'blocks/10')
    ))
def test_get_blocks(start_height, expected_url):
    blocks.get_blocks(start_height)
    blocks.get_from_path.assert_called_with(expected_url)


def test_get_last_block_height():
    blocks.get_last_block_height()
    blocks.get_from_path.assert_called_with('blocks/tip/height')


def test_get_last_block_hash():
    blocks.get_last_block_hash()
    blocks.get_from_path.assert_called_with('blocks/tip/hash')
