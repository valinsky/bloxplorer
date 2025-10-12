from bloxplorer import (
    sync_bitcoin_explorer, sync_bitcoin_signet_explorer, sync_bitcoin_testnet_explorer,
    sync_liquid_explorer
)
from bloxplorer.constants import (
    BITCOIN_API_BASE_URL, BITCOIN_SIGNET_API_BASE_URL, BITCOIN_TESTNET_API_BASE_URL,
    LIQUID_API_BASE_URL
)


def test_base_url():
    assert sync_bitcoin_explorer.base_url == BITCOIN_API_BASE_URL
    assert sync_bitcoin_testnet_explorer.base_url == BITCOIN_TESTNET_API_BASE_URL
    assert sync_bitcoin_signet_explorer.base_url == BITCOIN_SIGNET_API_BASE_URL
    assert sync_liquid_explorer.base_url == LIQUID_API_BASE_URL
