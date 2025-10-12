from unittest.mock import MagicMock

from bloxplorer.constants import BITCOIN_API_BASE_URL, http
from bloxplorer.mempool import SyncMempool

SyncMempool.make_request = MagicMock()
sync_mempool = SyncMempool(BITCOIN_API_BASE_URL)


def test_mempool():
    sync_mempool.get()
    sync_mempool.make_request.assert_called_with(http.GET, 'mempool')


def test_mempool_txids():
    sync_mempool.get_txids()
    sync_mempool.make_request.assert_called_with(http.GET, 'mempool/txids')


def test_mempool_latest_txs():
    sync_mempool.get_latest_txs()
    sync_mempool.make_request.assert_called_with(http.GET, 'mempool/recent')
