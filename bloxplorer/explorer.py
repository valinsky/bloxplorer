from bloxplorer.constants import (
    BITCOIN_API_BASE_URL, LIQUID_API_BASE_URL, BITCOIN_TESTNET_API_BASE_URL
)
from bloxplorer.addresses import Addresses
from bloxplorer.blocks import Blocks
from bloxplorer.fees import Fees
from bloxplorer.issued_assets import IssuedAssets
from bloxplorer.mempool import Mempool
from bloxplorer.transactions import Transactions


class BitcoinExplorer:
    """
    Wrapper class around the Bitcoin Esplora API.
    """
    BASE_URL = BITCOIN_API_BASE_URL

    def __init__(self):
        self.addr = Addresses(self.BASE_URL)
        self.tx = Transactions(self.BASE_URL)
        self.blocks = Blocks(self.BASE_URL)
        self.fees = Fees(self.BASE_URL)
        self.mempool = Mempool(self.BASE_URL)

    @property
    def base_url(self):
        return self.BASE_URL


class BitcoinTestnetExplorer(BitcoinExplorer):
    """
    Wrapper class around the Bitcoin Testnet Esplora API.
    """
    BASE_URL = BITCOIN_TESTNET_API_BASE_URL

    def __init__(self):
        super().__init__()


class LiquidExplorer(BitcoinExplorer):
    """
    Wrapper class around the Liquid Esplora API.
    """
    BASE_URL = LIQUID_API_BASE_URL

    def __init__(self):
        super().__init__()
        self.assets = IssuedAssets(self.BASE_URL)
