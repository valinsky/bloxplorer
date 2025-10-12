from bloxplorer.addresses import AsyncAddresses, SyncAddresses
from bloxplorer.blocks import AsyncBlocks, SyncBlocks
from bloxplorer.constants import (
    BITCOIN_API_BASE_URL, BITCOIN_SIGNET_API_BASE_URL, BITCOIN_TESTNET_API_BASE_URL,
    LIQUID_API_BASE_URL
)
from bloxplorer.fees import AsyncFees, SyncFees
from bloxplorer.issued_assets import AsyncIssuedAssets, SyncIssuedAssets
from bloxplorer.mempool import AsyncMempool, SyncMempool
from bloxplorer.transactions import AsyncTransactions, SyncTransactions


class SyncExplorer:
    BASE_URL = BITCOIN_API_BASE_URL

    def __init__(self):
        self.addr = SyncAddresses(self.BASE_URL)
        self.tx = SyncTransactions(self.BASE_URL)
        self.blocks = SyncBlocks(self.BASE_URL)
        self.fees = SyncFees(self.BASE_URL)
        self.mempool = SyncMempool(self.BASE_URL)

    @property
    def base_url(self):
        return self.BASE_URL


class AsyncExplorer(SyncExplorer):
    def __init__(self):
        self.addr = AsyncAddresses(self.BASE_URL)
        self.tx = AsyncTransactions(self.BASE_URL)
        self.blocks = AsyncBlocks(self.BASE_URL)
        self.fees = AsyncFees(self.BASE_URL)
        self.mempool = AsyncMempool(self.BASE_URL)


class SyncBitcoinExplorer(SyncExplorer):
    BASE_URL = BITCOIN_API_BASE_URL


class AsyncBitcoinExplorer(AsyncExplorer):
    BASE_URL = BITCOIN_API_BASE_URL


class SyncBitcoinTestnetExplorer(SyncExplorer):
    BASE_URL = BITCOIN_TESTNET_API_BASE_URL


class AsyncBitcoinTestnetExplorer(AsyncExplorer):
    BASE_URL = BITCOIN_TESTNET_API_BASE_URL


class SyncBitcoinSignetExplorer(SyncExplorer):
    BASE_URL = BITCOIN_SIGNET_API_BASE_URL


class AsyncBitcoinSignetExplorer(AsyncExplorer):
    BASE_URL = BITCOIN_SIGNET_API_BASE_URL


class SyncLiquidExplorer(SyncExplorer):
    BASE_URL = LIQUID_API_BASE_URL

    def __init__(self):
        super().__init__()
        self.assets = SyncIssuedAssets(self.BASE_URL)


class AsyncLiquidExplorer(AsyncExplorer):
    BASE_URL = LIQUID_API_BASE_URL

    def __init__(self):
        super().__init__()
        self.assets = AsyncIssuedAssets(self.BASE_URL)
