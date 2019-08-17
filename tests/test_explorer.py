from bloxplorer.constants import (
    BITCOIN_API_BASE_URL, LIQUID_API_BASE_URL, BITCOIN_TESTNET_API_BASE_URL
)
from bloxplorer import bitcoin_explorer, bitcoin_testnet_explorer, liquid_explorer


def test_base_url():
    assert bitcoin_explorer.base_url == BITCOIN_API_BASE_URL
    assert bitcoin_testnet_explorer.base_url == BITCOIN_TESTNET_API_BASE_URL
    assert liquid_explorer.base_url == LIQUID_API_BASE_URL
