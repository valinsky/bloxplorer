from unittest.mock import MagicMock

import pytest

from blockstreamesplora.addresses import Addresses


Addresses.get_from_path = MagicMock()
addresses = Addresses()

def test_get_address():
    address = '1234'
    addresses.get_address(address)
    addresses.get_from_path.assert_called_with('address/1234')

def test_get_scripthash():
    hash = '1234'
    addresses.get_scripthash(hash)
    addresses.get_from_path.assert_called_with('scripthash/1234')

@pytest.mark.parametrize(
    'address, last_seen_txid, expected_url', (
        ('1234', None, 'address/1234/txs'),
        ('1234', '4321', 'address/1234/txs/chain/4321')
    ))
def test_get_address_tx_history(address, last_seen_txid, expected_url):
    addresses.get_address_tx_history(address, last_seen_txid)
    addresses.get_from_path.assert_called_with(expected_url)

@pytest.mark.parametrize(
    'hash, last_seen_txid, expected_url', (
        ('1234', None, 'scripthash/1234/txs'),
        ('1234', '4321', 'scripthash/1234/txs/chain/4321')
    ))
def test_get_scripthash_tx_history(hash, last_seen_txid, expected_url):
    addresses.get_scripthash_tx_history(hash, last_seen_txid)
    addresses.get_from_path.assert_called_with(expected_url)

def test_get_address_unconfirmed_tx_history():
    address = '1234'
    addresses.get_address_unconfirmed_tx_history(address)
    addresses.get_from_path.assert_called_with('address/1234/txs/mempool')

def test_get_scripthash_unconfirmed_tx_history():
    hash = '1234'
    addresses.get_scripthash_unconfirmed_tx_history(hash)
    addresses.get_from_path.assert_called_with('scripthash/1234/txs/mempool')

def test_get_address_utxo():
    address = '1234'
    addresses.get_address_utxo(address)
    addresses.get_from_path.assert_called_with('address/1234/utxo')

def test_get_scripthash_utxo():
    hash = '1234'
    addresses.get_scripthash_utxo(hash)
    addresses.get_from_path.assert_called_with('scripthash/1234/utxo')
