import asyncio

from unittest.mock import AsyncMock, MagicMock

from bloxplorer.constants import BITCOIN_API_BASE_URL, http
from bloxplorer.mempool import AsyncMempool, SyncMempool

SyncMempool.make_request = MagicMock()
sync_mempool = SyncMempool(BITCOIN_API_BASE_URL)


def test_mempool_sync():
    sync_mempool.get()
    sync_mempool.make_request.assert_called_with(http.GET, 'mempool')


def test_mempool_txids_sync():
    sync_mempool.get_txids()
    sync_mempool.make_request.assert_called_with(http.GET, 'mempool/txids')


def test_mempool_latest_txs_sync():
    sync_mempool.get_latest_txs()
    sync_mempool.make_request.assert_called_with(http.GET, 'mempool/recent')


AsyncMempool.make_request = AsyncMock()
async_mempool = AsyncMempool(BITCOIN_API_BASE_URL)


def test_mempool_async():
    asyncio.run(async_mempool.get())
    async_mempool.make_request.assert_called_with(http.GET, 'mempool')


def test_mempool_txids_async():
    asyncio.run(async_mempool.get_txids())
    async_mempool.make_request.assert_called_with(http.GET, 'mempool/txids')


def test_mempool_latest_txs_async():
    asyncio.run(async_mempool.get_latest_txs())
    async_mempool.make_request.assert_called_with(http.GET, 'mempool/recent')
