import pytest

from bloxplorer import bitcoin_explorer, bitcoin_testnet_explorer, liquid_explorer
from bloxplorer.constants import (
    BECH32, BIP32_PRVKEY, BIP32_PUBKEY, BITCOIN_API_BASE_URL, BITCOIN_TESTNET_API_BASE_URL,
    LIQUID_API_BASE_URL, P2PKH, P2SH, UNRECOGNIZED_ADDRESS_TYPE
)


def test_base_url():
    assert bitcoin_explorer.base_url == BITCOIN_API_BASE_URL
    assert bitcoin_testnet_explorer.base_url == BITCOIN_TESTNET_API_BASE_URL
    assert liquid_explorer.base_url == LIQUID_API_BASE_URL


@pytest.mark.parametrize(
    'address, expected_value', (
        (b'17VZNX1SN5NtKa8UQFxwQbFeFc3iqRYhem', P2PKH),
        ('17VZNX1SN5NtKa8UQFxwQbFeFc3iqRYhem', P2PKH),
        ('3EktnHQD7RiAE6uzMj2ZifT9YgRrkSgzQX', P2SH),
        ('bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4', BECH32),
        ('xpub661MyMwAqRbcEYS8w7XLSVeEsBXy79zSzH1J8vCdxAZningWLdN3zgtU6LBpB85b3D2yc8sfvZU521AAwdZafEz7mnzBBsz4wKY5e4cp9LB', BIP32_PUBKEY),
        ('xprv9s21ZrQH143K24Mfq5zL5MhWK9hUhhGbd45hLXo2Pq2oqzMMo63oStZzF93Y5wvzdUayhgkkFoicQZcP3y52uPPxFnfoLZB21Teqt1VvEHx', BIP32_PRVKEY),
        ('the cake is a lie', UNRECOGNIZED_ADDRESS_TYPE),
    )
)
def test_get_address_type_mainnet(address, expected_value):
    assert bitcoin_explorer.get_address_type(address) == expected_value


@pytest.mark.parametrize(
    'address, expected_value', (
        (b'mipcBbFg9gMiCh81Kj8tqqdgoZub1ZJRfn', P2PKH),
        ('mipcBbFg9gMiCh81Kj8tqqdgoZub1ZJRfn', P2PKH),
        ('nipcBbFg9gMiCh81Kj8tqqdgoZub1ZJRfn', P2PKH),
        ('2MzQwSSnBHWHqSAqtTVQ6v47XtaisrJa1Vc ', P2SH),
        ('tb1qw508d6qejxtdg4y5r3zarvary0c5xw7kxpjzsx', BECH32),
        ('tpubD6NzVbkrYhZ4WLczPJWReQycCJdd6YVWXubbVUFnJ5KgU5MDQrD998ZJLNGbhd2pq7ZtDiPYTfJ7iBenLVQpYgSQqPjUsQeJXH8VQ8xA67D', BIP32_PUBKEY),
        ('tprv8ZgxMBicQKsPcsbCVeqqF1KVdH7gwDJbxbzpCxDUsoXHdb6SnTPYxdwSAKDC6KKJzv7khnNWRAJQsRA8BBQyiSfYnRt6zuu4vZQGKjeW4YF', BIP32_PRVKEY),
        ('the cake is indeed a lie', UNRECOGNIZED_ADDRESS_TYPE),
    )
)
def test_get_address_type_testnet(address, expected_value):
    assert bitcoin_testnet_explorer.get_address_type(address) == expected_value


def test_get_address_type_liquid():
    with pytest.raises(AttributeError):
        assert liquid_explorer.get_address_type('address')
