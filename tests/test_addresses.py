from unittest.mock import MagicMock

import pytest

from bloxplorer.addresses import Addresses
from bloxplorer.constants import BITCOIN_API_BASE_URL, http

Addresses.make_request = MagicMock()
addresses = Addresses(BITCOIN_API_BASE_URL)


def test_get_address():
    address = '1234'
    addresses.get(address)
    addresses.make_request.assert_called_with(http.GET, 'address/1234')


def test_get_scripthash():
    hash = '1234'
    addresses.get_scripthash(hash)
    addresses.make_request.assert_called_with(http.GET, 'scripthash/1234')


def test_get_address_tx_history():
    address = '1234'
    addresses.get_tx_history(address)
    addresses.make_request.assert_called_with(http.GET, 'address/1234/txs')


def test_get_scripthash_tx_history():
    hash = '1234'
    addresses.get_scripthash_tx_history(hash)
    addresses.make_request.assert_called_with(http.GET, 'scripthash/1234/txs')


@pytest.mark.parametrize(
    'address, last_seen_txid, expected_url', (
        ('1234', None, 'address/1234/txs/chain'),
        ('1234', '4321', 'address/1234/txs/chain/4321')
    ))
def test_get_confirmed_tx_history(address, last_seen_txid, expected_url):
    addresses.get_confirmed_tx_history(address, last_seen_txid)
    addresses.make_request.assert_called_with(http.GET, expected_url)


@pytest.mark.parametrize(
    'hash, last_seen_txid, expected_url', (
        ('1234', None, 'scripthash/1234/txs/chain'),
        ('1234', '4321', 'scripthash/1234/txs/chain/4321')
    ))
def test_get_confirmed_scripthash_tx_history(hash, last_seen_txid, expected_url):
    addresses.get_confirmed_scripthash_tx_history(hash, last_seen_txid)
    addresses.make_request.assert_called_with(http.GET, expected_url)


def test_get_address_unconfirmed_tx_history():
    address = '1234'
    addresses.get_unconfirmed_tx_history(address)
    addresses.make_request.assert_called_with(http.GET, 'address/1234/txs/mempool')


def test_get_scripthash_unconfirmed_tx_history():
    hash = '1234'
    addresses.get_unconfirmed_scripthash_tx_history(hash)
    addresses.make_request.assert_called_with(http.GET, 'scripthash/1234/txs/mempool')


def test_get_address_utxo():
    address = '1234'
    addresses.get_utxo(address)
    addresses.make_request.assert_called_with(http.GET, 'address/1234/utxo')


def test_get_scripthash_utxo():
    hash = '1234'
    addresses.get_scripthash_utxo(hash)
    addresses.make_request.assert_called_with(http.GET, 'scripthash/1234/utxo')


def test_get_address_prefix():
    prefix = 'pre'
    addresses.get_address_prefix(prefix)
    addresses.make_request.assert_called_with(http.GET, f'address-prefix/{prefix}')
