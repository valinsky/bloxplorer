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

    >>> from bloxplorer import bitcoin_explorer
    >>> response = await bitcoin_explorer.blocks.get_last_height()
    >>> print(response.data)
    '586438'
"""

sync_bitcoin_explorer = SyncBitcoinExplorer()
sync_bitcoin_testnet_explorer = SyncBitcoinTestnetExplorer()
sync_bitcoin_signet_explorer = SyncBitcoinSignetExplorer()
sync_liquid_explorer = SyncLiquidExplorer()

async_bitcoin_explorer = AsyncBitcoinExplorer()
async_bitcoin_testnet_explorer = AsyncBitcoinTestnetExplorer()
async_bitcoin_signet_explorer = AsyncBitcoinSignetExplorer()
async_liquid_explorer = AsyncLiquidExplorer()
