from bloxplorer import (
    bitcoin_explorer, bitcoin_signet_explorer, bitcoin_testnet_explorer,
    liquid_explorer, async_bitcoin_explorer, async_bitcoin_signet_explorer,
    async_bitcoin_testnet_explorer, async_liquid_explorer
)
from bloxplorer.constants import (
    BITCOIN_API_BASE_URL, BITCOIN_SIGNET_API_BASE_URL, BITCOIN_TESTNET_API_BASE_URL,
    LIQUID_API_BASE_URL
)


def test_base_url():
    assert bitcoin_explorer.base_url == BITCOIN_API_BASE_URL
    assert bitcoin_testnet_explorer.base_url == BITCOIN_TESTNET_API_BASE_URL
    assert bitcoin_signet_explorer.base_url == BITCOIN_SIGNET_API_BASE_URL
    assert liquid_explorer.base_url == LIQUID_API_BASE_URL

    assert async_bitcoin_explorer.base_url == BITCOIN_API_BASE_URL
    assert async_bitcoin_testnet_explorer.base_url == BITCOIN_TESTNET_API_BASE_URL
    assert async_bitcoin_signet_explorer.base_url == BITCOIN_SIGNET_API_BASE_URL
    assert async_liquid_explorer.base_url == LIQUID_API_BASE_URL
