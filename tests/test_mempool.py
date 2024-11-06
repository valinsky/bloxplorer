from unittest.mock import MagicMock

from bloxplorer.constants import BITCOIN_API_BASE_URL, http
from bloxplorer.mempool import Mempool

Mempool.make_request = MagicMock()
mempool = Mempool(BITCOIN_API_BASE_URL)


def test_mempool():
    mempool.get()
    mempool.make_request.assert_called_with(http.GET, 'mempool')


def test_mempool_txids():
    mempool.get_txids()
    mempool.make_request.assert_called_with(http.GET, 'mempool/txids')


def test_mempool_latest_txs():
    mempool.get_latest_txs()
    mempool.make_request.assert_called_with(http.GET, 'mempool/recent')
