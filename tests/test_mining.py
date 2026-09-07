import asyncio

from unittest.mock import AsyncMock, MagicMock

from bloxplorer.constants import BITCOIN_API_BASE_URL, http
from bloxplorer.mining import AsyncMining, SyncMining

SyncMining.make_request = MagicMock()
sync_mining = SyncMining(BITCOIN_API_BASE_URL)


def test_get_block_template_sync():
    sync_mining.get_block_template()
    sync_mining.make_request.assert_called_with(http.GET, 'block-template')


AsyncMining.make_request = AsyncMock()
async_mining = AsyncMining(BITCOIN_API_BASE_URL)


def test_get_block_template_async():
    asyncio.run(async_mining.get_block_template())
    async_mining.make_request.assert_called_with(http.GET, 'block-template')
