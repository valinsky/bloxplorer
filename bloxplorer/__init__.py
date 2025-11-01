from bloxplorer.explorers import (
    AsyncBitcoinExplorer, AsyncBitcoinSignetExplorer, AsyncBitcoinTestnetExplorer,
    AsyncLiquidExplorer, SyncBitcoinExplorer, SyncBitcoinSignetExplorer, SyncBitcoinTestnetExplorer,
    SyncLiquidExplorer
)

"""
Sync Usage::

    >>> from bloxplorer import bitcoin_explorer
    >>> response = bitcoin_explorer.blocks.get_last_height()
    >>> print(response.data)
    '586438'


Async Usage::

    >>> from bloxplorer import async_bitcoin_explorer
    >>> response = await async_bitcoin_explorer.blocks.get_last_height()
    >>> print(response.data)
    '586438'
"""

bitcoin_explorer = SyncBitcoinExplorer()
bitcoin_testnet_explorer = SyncBitcoinTestnetExplorer()
bitcoin_signet_explorer = SyncBitcoinSignetExplorer()
liquid_explorer = SyncLiquidExplorer()

async_bitcoin_explorer = AsyncBitcoinExplorer()
async_bitcoin_testnet_explorer = AsyncBitcoinTestnetExplorer()
async_bitcoin_signet_explorer = AsyncBitcoinSignetExplorer()
async_liquid_explorer = AsyncLiquidExplorer()
