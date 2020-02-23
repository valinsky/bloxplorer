from bloxplorer.addresses import Addresses
from bloxplorer.blocks import Blocks
from bloxplorer.constants import (
    BECH32, BIP32_PRVKEY, BIP32_PUBKEY, BITCOIN_API_BASE_URL, BITCOIN_TESTNET_API_BASE_URL,
    LIQUID_API_BASE_URL, P2PKH, P2SH, UNRECOGNIZED_ADDRESS_TYPE
)
from bloxplorer.fees import Fees
from bloxplorer.issued_assets import IssuedAssets
from bloxplorer.mempool import Mempool
from bloxplorer.transactions import Transactions


class Explorer:
    """
    Parent Explorer class.
    Uses the Bitcoin API URL as default.
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


class BitcoinExplorer(Explorer):

    BASE_URL = BITCOIN_API_BASE_URL

    def __init__(self):
        super().__init__()

    @staticmethod
    def get_address_type(address):
        """
        Get the Bitcoin address type.

        :param address: The alphanumeric Bitcoin address

        :return: String representing the address type (P2PKH, P2SH, etc.)
        """
        if isinstance(address, bytes):
            address = address.decode()

        if address[0] == '1':
            return P2PKH
        if address[0] == '3':
            return P2SH
        if address[:3] == 'bc1':
            return BECH32
        if address[:4] == 'xpub':
            return BIP32_PUBKEY
        if address[:4] == 'xprv':
            return BIP32_PRVKEY

        return UNRECOGNIZED_ADDRESS_TYPE


class BitcoinTestnetExplorer(Explorer):

    BASE_URL = BITCOIN_TESTNET_API_BASE_URL

    def __init__(self):
        super().__init__()

    @staticmethod
    def get_address_type(address):
        """
        Get the Bitcoin Testnet address type.

        :param address: The alphanumeric Bitcoin address

        :return: String representing the address type (P2PKH, P2SH, etc.)
        """
        if isinstance(address, bytes):
            address = address.decode()

        if address[0] in ('m', 'n'):
            return P2PKH
        if address[0] == '2':
            return P2SH
        if address[:3] == 'tb1':
            return BECH32
        if address[:4] == 'tpub':
            return BIP32_PUBKEY
        if address[:4] == 'tprv':
            return BIP32_PRVKEY

        return UNRECOGNIZED_ADDRESS_TYPE


class LiquidExplorer(Explorer):
    """
    Liquid also uses the Issued Assets feature.
    """

    BASE_URL = LIQUID_API_BASE_URL

    def __init__(self):
        super().__init__()
        self.assets = IssuedAssets(self.BASE_URL)
