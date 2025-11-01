import asyncio

from unittest.mock import AsyncMock, MagicMock

import pytest

from bloxplorer.addresses import AsyncAddresses, SyncAddresses
from bloxplorer.constants import BITCOIN_API_BASE_URL, http

SyncAddresses.make_request = MagicMock()
sync_addresses = SyncAddresses(BITCOIN_API_BASE_URL)


def test_get_address_sync():
    address = '1234'
    sync_addresses.get(address)
    sync_addresses.make_request.assert_called_with(http.GET, 'address/1234')


def test_get_scripthash_sync():
    hash = '1234'
    sync_addresses.get_scripthash(hash)
    sync_addresses.make_request.assert_called_with(http.GET, 'scripthash/1234')


def test_get_address_tx_history_sync():
    address = '1234'
    sync_addresses.get_tx_history(address)
    sync_addresses.make_request.assert_called_with(http.GET, 'address/1234/txs')


def test_get_scripthash_tx_history_sync():
    hash = '1234'
    sync_addresses.get_scripthash_tx_history(hash)
    sync_addresses.make_request.assert_called_with(http.GET, 'scripthash/1234/txs')


@pytest.mark.parametrize(
    'address, last_seen_txid, expected_url', (
        ('1234', None, 'address/1234/txs/chain'),
        ('1234', '4321', 'address/1234/txs/chain/4321')
    ))
def test_get_confirmed_tx_history_sync(address, last_seen_txid, expected_url):
    sync_addresses.get_confirmed_tx_history(address, last_seen_txid)
    sync_addresses.make_request.assert_called_with(http.GET, expected_url)


@pytest.mark.parametrize(
    'hash, last_seen_txid, expected_url', (
        ('1234', None, 'scripthash/1234/txs/chain'),
        ('1234', '4321', 'scripthash/1234/txs/chain/4321')
    ))
def test_get_confirmed_scripthash_tx_history_sync(hash, last_seen_txid, expected_url):
    sync_addresses.get_confirmed_scripthash_tx_history(hash, last_seen_txid)
    sync_addresses.make_request.assert_called_with(http.GET, expected_url)


def test_get_address_unconfirmed_tx_history_sync():
    address = '1234'
    sync_addresses.get_unconfirmed_tx_history(address)
    sync_addresses.make_request.assert_called_with(http.GET, 'address/1234/txs/mempool')


def test_get_scripthash_unconfirmed_tx_history_sync():
    hash = '1234'
    sync_addresses.get_unconfirmed_scripthash_tx_history(hash)
    sync_addresses.make_request.assert_called_with(http.GET, 'scripthash/1234/txs/mempool')


def test_get_address_utxo_sync():
    address = '1234'
    sync_addresses.get_utxo(address)
    sync_addresses.make_request.assert_called_with(http.GET, 'address/1234/utxo')


def test_get_scripthash_utxo_sync():
    hash = '1234'
    sync_addresses.get_scripthash_utxo(hash)
    sync_addresses.make_request.assert_called_with(http.GET, 'scripthash/1234/utxo')


def test_get_address_prefix_sync():
    prefix = 'pre'
    sync_addresses.get_address_prefix(prefix)
    sync_addresses.make_request.assert_called_with(http.GET, f'address-prefix/{prefix}')


AsyncAddresses.make_request = AsyncMock()
async_addresses = AsyncAddresses(BITCOIN_API_BASE_URL)


def test_get_address_async():
    address = '1234'
    asyncio.run(async_addresses.get(address))
    async_addresses.make_request.assert_called_with(http.GET, 'address/1234')


def test_get_scripthash_async():
    hash = '1234'
    asyncio.run(async_addresses.get_scripthash(hash))
    async_addresses.make_request.assert_called_with(http.GET, 'scripthash/1234')


def test_get_address_tx_history_async():
    address = '1234'
    asyncio.run(async_addresses.get_tx_history(address))
    async_addresses.make_request.assert_called_with(http.GET, 'address/1234/txs')


def test_get_scripthash_tx_history_async():
    hash = '1234'
    asyncio.run(async_addresses.get_scripthash_tx_history(hash))
    async_addresses.make_request.assert_called_with(http.GET, 'scripthash/1234/txs')


@pytest.mark.parametrize(
    'address, last_seen_txid, expected_url', (
        ('1234', None, 'address/1234/txs/chain'),
        ('1234', '4321', 'address/1234/txs/chain/4321')
    ))
def test_get_confirmed_tx_history_async(address, last_seen_txid, expected_url):
    asyncio.run(async_addresses.get_confirmed_tx_history(address, last_seen_txid))
    async_addresses.make_request.assert_called_with(http.GET, expected_url)


@pytest.mark.parametrize(
    'hash, last_seen_txid, expected_url', (
        ('1234', None, 'scripthash/1234/txs/chain'),
        ('1234', '4321', 'scripthash/1234/txs/chain/4321')
    ))
def test_get_confirmed_scripthash_tx_history_async(hash, last_seen_txid, expected_url):
    asyncio.run(async_addresses.get_confirmed_scripthash_tx_history(hash, last_seen_txid))
    async_addresses.make_request.assert_called_with(http.GET, expected_url)


def test_get_address_unconfirmed_tx_history_async():
    address = '1234'
    asyncio.run(async_addresses.get_unconfirmed_tx_history(address))
    async_addresses.make_request.assert_called_with(http.GET, 'address/1234/txs/mempool')


def test_get_scripthash_unconfirmed_tx_history_async():
    hash = '1234'
    asyncio.run(async_addresses.get_unconfirmed_scripthash_tx_history(hash))
    async_addresses.make_request.assert_called_with(http.GET, 'scripthash/1234/txs/mempool')


def test_get_address_utxo_async():
    address = '1234'
    asyncio.run(async_addresses.get_utxo(address))
    async_addresses.make_request.assert_called_with(http.GET, 'address/1234/utxo')


def test_get_scripthash_utxo_async():
    hash = '1234'
    asyncio.run(async_addresses.get_scripthash_utxo(hash))
    async_addresses.make_request.assert_called_with(http.GET, 'scripthash/1234/utxo')


def test_get_address_prefix_async():
    prefix = 'pre'
    asyncio.run(async_addresses.get_address_prefix(prefix))
    async_addresses.make_request.assert_called_with(http.GET, f'address-prefix/{prefix}')
