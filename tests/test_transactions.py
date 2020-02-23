from unittest.mock import MagicMock

import pytest

from bloxplorer.constants import BITCOIN_API_BASE_URL
from bloxplorer.transactions import Transactions

Transactions.make_request = MagicMock()
transactions = Transactions(BITCOIN_API_BASE_URL)


def test_get_tx():
    tx_id = '1234'
    transactions.get(tx_id)
    transactions.make_request.assert_called_with('GET', f'tx/{tx_id}')


def test_get_tx_status():
    tx_id = '1234'
    transactions.get_status(tx_id)
    transactions.make_request.assert_called_with('GET', f'tx/{tx_id}/status')


def test_get_tx_raw_hex():
    tx_id = '1234'
    transactions.get_raw(tx_id)
    transactions.make_request.assert_called_with('GET', f'tx/{tx_id}/hex')


def test_get_tx_merkle_proof():
    tx_id = '1234'
    transactions.get_merkle_proof(tx_id)
    transactions.make_request.assert_called_with('GET', f'tx/{tx_id}/merkle-proof')


@pytest.mark.parametrize(
    'tx_id, vout', (
        ('1234', None),
        ('1234', 1)
    ))
def test_get_spending_status(tx_id, vout):
    path = f'tx/{tx_id}/outspend/{vout}' if vout is not None else f'tx/{tx_id}/outspends'
    transactions.get_spending_status(tx_id, vout)
    transactions.make_request.assert_called_with('GET', path)


def test_post_tx():
    tx_hex = hex(1234567890)
    transactions.post(tx_hex)
    transactions.make_request.assert_called_with('POST', 'tx', data=tx_hex)
