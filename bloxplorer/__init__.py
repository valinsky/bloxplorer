from bloxplorer.explorer import (
    BitcoinExplorer, BitcoinSignetExplorer, BitcoinTestnetExplorer, LiquidExplorer
)

"""
Usage::

    >>> from bloxplorer import bitcoin_explorer
    >>> response = bitcoin_explorer.blocks.get_last_height()
    >>> print(response.data)
    '586438'
"""

bitcoin_explorer = BitcoinExplorer()
bitcoin_testnet_explorer = BitcoinTestnetExplorer()
bitcoin_signet_explorer = BitcoinSignetExplorer()
liquid_explorer = LiquidExplorer()
