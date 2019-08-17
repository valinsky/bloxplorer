from bloxplorer.explorer import BitcoinExplorer, LiquidExplorer, BitcoinTestnetExplorer


__version__ = '0.1.0'

"""
Usage::

    >>> from bloxplorer import bitcoin_explorer
    >>> response = bitcoin_explorer.blocks.get_last_height()
    >>> print(response.data)
    '586438'
"""

bitcoin_explorer = BitcoinExplorer()
bitcoin_testnet_explorer = BitcoinTestnetExplorer()
liquid_explorer = LiquidExplorer()
