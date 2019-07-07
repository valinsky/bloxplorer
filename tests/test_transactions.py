from unittest.mock import MagicMock

from blockstreamesplora.transactions import Transactions


Transactions.get_from_path = MagicMock()
transactions = Transactions()


def test_get_tx():
    tx_id = '1234'
    transactions.get_tx(tx_id)
    transactions.get_from_path.assert_called_with(f'tx/{tx_id}')


def test_get_tx_status():
    tx_id = '1234'
    transactions.get_tx_status(tx_id)
    transactions.get_from_path.assert_called_with(f'tx/{tx_id}/status')


def test_get_tx_raw_hex():
    tx_id = '1234'
    transactions.get_tx_raw_hex(tx_id)
    transactions.get_from_path.assert_called_with(f'tx/{tx_id}/hex')


def test_get_tx_merkle_proof():
    tx_id = '1234'
    transactions.get_tx_merkle_proof(tx_id)
    transactions.get_from_path.assert_called_with(f'tx/{tx_id}/merkle-proof')


def test_get_tx_ouput_status():
    tx_id, vout = '1234', 12
    transactions.get_tx_output_status(tx_id, vout)
    transactions.get_from_path.assert_called_with(f'tx/{tx_id}/outspend/{vout}')


def test_get_tx_outspends():
    tx_id = '1234'
    transactions.get_tx_outspends(tx_id)
    transactions.get_from_path.assert_called_with(f'tx/{tx_id}/outspends')


def test_post_tx():
    pass
