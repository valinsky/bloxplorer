import asyncio

from unittest.mock import AsyncMock, MagicMock

import pytest

from bloxplorer.constants import BITCOIN_API_BASE_URL, http
from bloxplorer.transactions import AsyncTransactions, SyncTransactions

SyncTransactions.make_request = MagicMock()
sync_transactions = SyncTransactions(BITCOIN_API_BASE_URL)


def test_get_tx_sync():
    tx_id = '1234'
    sync_transactions.get(tx_id)
    sync_transactions.make_request.assert_called_with(http.GET, f'tx/{tx_id}')


def test_get_tx_status_sync():
    tx_id = '1234'
    sync_transactions.get_status(tx_id)
    sync_transactions.make_request.assert_called_with(http.GET, f'tx/{tx_id}/status')


def test_get_tx_raw_sync():
    tx_id = '1234'
    sync_transactions.get_raw(tx_id)
    sync_transactions.make_request.assert_called_with(http.GET, f'tx/{tx_id}/raw')


def test_get_tx_hex_sync():
    tx_id = '1234'
    sync_transactions.get_hex(tx_id)
    sync_transactions.make_request.assert_called_with(http.GET, f'tx/{tx_id}/hex')


def test_get_tx_merkleblock_proof_sync():
    tx_id = '1234'
    sync_transactions.get_merkleblock_proof(tx_id)
    sync_transactions.make_request.assert_called_with(http.GET, f'tx/{tx_id}/merkleblock-proof')


def test_get_tx_merkle_proof_sync():
    tx_id = '1234'
    sync_transactions.get_merkle_proof(tx_id)
    sync_transactions.make_request.assert_called_with(http.GET, f'tx/{tx_id}/merkle-proof')


@pytest.mark.parametrize(
    'tx_id, vout', (
        ('1234', None),
        ('1234', 1)
    ))
def test_get_spending_status_sync(tx_id, vout):
    path = f'tx/{tx_id}/outspend/{vout}' if vout is not None else f'tx/{tx_id}/outspends'
    sync_transactions.get_spending_status(tx_id, vout)
    sync_transactions.make_request.assert_called_with(http.GET, path)


def test_post_tx_sync():
    tx_hex = hex(1234567890)
    sync_transactions.post(tx_hex)
    sync_transactions.make_request.assert_called_with(http.POST, 'tx', data=tx_hex)


def test_post_tx_package_sync():
    tx_hexes = ['02000000...', '02000000...']
    sync_transactions.post_package(tx_hexes)
    sync_transactions.make_request.assert_called_with(http.POST, 'txs/package', json=tx_hexes)


def test_post_tx_package_sync_accepts_iterable():
    tx_hexes = iter(['02000000...', '02000000...'])
    sync_transactions.post_package(tx_hexes)
    sync_transactions.make_request.assert_called_with(
        http.POST, 'txs/package', json=['02000000...', '02000000...']
    )


AsyncTransactions.make_request = AsyncMock()
async_transactions = AsyncTransactions(BITCOIN_API_BASE_URL)


def test_get_tx_async():
    tx_id = '1234'
    asyncio.run(async_transactions.get(tx_id))
    async_transactions.make_request.assert_called_with(http.GET, f'tx/{tx_id}')


def test_get_tx_status_async():
    tx_id = '1234'
    asyncio.run(async_transactions.get_status(tx_id))
    async_transactions.make_request.assert_called_with(http.GET, f'tx/{tx_id}/status')


def test_get_tx_raw_async():
    tx_id = '1234'
    asyncio.run(async_transactions.get_raw(tx_id))
    async_transactions.make_request.assert_called_with(http.GET, f'tx/{tx_id}/raw')


def test_get_tx_hex_async():
    tx_id = '1234'
    asyncio.run(async_transactions.get_hex(tx_id))
    async_transactions.make_request.assert_called_with(http.GET, f'tx/{tx_id}/hex')


def test_get_tx_merkleblock_proof_async():
    tx_id = '1234'
    asyncio.run(async_transactions.get_merkleblock_proof(tx_id))
    async_transactions.make_request.assert_called_with(http.GET, f'tx/{tx_id}/merkleblock-proof')


def test_get_tx_merkle_proof_async():
    tx_id = '1234'
    asyncio.run(async_transactions.get_merkle_proof(tx_id))
    async_transactions.make_request.assert_called_with(http.GET, f'tx/{tx_id}/merkle-proof')


@pytest.mark.parametrize(
    'tx_id, vout', (
        ('1234', None),
        ('1234', 1)
    ))
def test_get_spending_status_async(tx_id, vout):
    path = f'tx/{tx_id}/outspend/{vout}' if vout is not None else f'tx/{tx_id}/outspends'
    asyncio.run(async_transactions.get_spending_status(tx_id, vout))
    async_transactions.make_request.assert_called_with(http.GET, path)


def test_post_tx_async():
    tx_hex = hex(1234567890)
    asyncio.run(async_transactions.post(tx_hex))
    async_transactions.make_request.assert_called_with(http.POST, 'tx', data=tx_hex)


def test_post_tx_package_async():
    tx_hexes = ['02000000...', '02000000...']
    asyncio.run(async_transactions.post_package(tx_hexes))
    async_transactions.make_request.assert_called_with(http.POST, 'txs/package', json=tx_hexes)


def test_post_tx_package_async_accepts_iterable():
    tx_hexes = iter(['02000000...', '02000000...'])
    asyncio.run(async_transactions.post_package(tx_hexes))
    async_transactions.make_request.assert_called_with(
        http.POST, 'txs/package', json=['02000000...', '02000000...']
    )
