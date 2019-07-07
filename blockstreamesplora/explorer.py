from blockstreamesplora.constants import BITCOIN_API_BASE_URL, LIQUID_API_BASE_URL
from blockstreamesplora.addresses import Addresses
from blockstreamesplora.blocks import Blocks
from blockstreamesplora.mempool import Mempool
from blockstreamesplora.transactions import Transactions
from blockstreamesplora.fees import Fees


class BitcoinExplorer(Transactions, Addresses, Blocks, Mempool, Fees):
    BASE_API_URL = BITCOIN_API_BASE_URL


class LiquidExplorer(BitcoinExplorer):
    BASE_API_URL = LIQUID_API_BASE_URL
