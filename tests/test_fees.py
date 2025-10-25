import asyncio

from unittest.mock import AsyncMock, MagicMock

from bloxplorer.constants import BITCOIN_API_BASE_URL, http
from bloxplorer.fees import AsyncFees, SyncFees


SyncFees.make_request = MagicMock()
sync_fees = SyncFees(BITCOIN_API_BASE_URL)

def test_get_address_sync():
    sync_fees.get_estimates()
    sync_fees.make_request.assert_called_with(http.GET, 'fee-estimates')


AsyncFees.make_request = AsyncMock()
async_fees = AsyncFees(BITCOIN_API_BASE_URL)

def test_get_addresses_async():
    asyncio.run(async_fees.get_estimates())
    async_fees.make_request.assert_called_with(http.GET, 'fee-estimates')