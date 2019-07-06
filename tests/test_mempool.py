from unittest.mock import MagicMock

import pytest

from blockstreamesplora.mempool import Mempool


Mempool.get_from_path = MagicMock()
mempool = Mempool()

def test_mempool():
    mempool.get_mempool()
    mempool.get_from_path.assert_called_with('mempool')

def test_mempool_txids():
    mempool.get_mempool_txids()
    mempool.get_from_path.assert_called_with('mempool/txids')

def test_mempool_latest_txs():
    mempool.get_mempool_latest_txs()
    mempool.get_from_path.assert_called_with('mempool/recent')