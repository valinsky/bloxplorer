from bloxplorer.utils import Request


class Transactions(Request):
    """
    Wrapper class around the Esplora Transactions endpoint.

    `Blockstream Esplora Transactions API Docs
    <https://github.com/Blockstream/esplora/blob/master/API.md#transactions>`_
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self, tx_id, **kwargs):
        r"""
        Returns information about the transaction.

        :param tx_id: String representing the transaction hash.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'tx/{tx_id}', **kwargs)

    def get_status(self, tx_id, **kwargs):
        r"""
        Returns the transaction confirmation status

        :param tx_id: String representing the transaction hash.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'tx/{tx_id}/status', **kwargs)

    def get_raw(self, tx_id, **kwargs):
        r"""
        Returns the transaction as binary data.

        :param tx_id: String representing the transaction hash.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'tx/{tx_id}/raw', **kwargs)

    def get_hex(self, tx_id, **kwargs):
        r"""
        Returns the transaction in hex.

        :param tx_id: String representing the transaction hash.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'tx/{tx_id}/hex', **kwargs)

    def get_merkleblock_proof(self, tx_id, **kwargs):
        r"""
        Returns a merkle inclusion proof for the transaction using
        `bitcoind's merkleblock <https://bitcoin.org/en/glossary/merkle-block>`_ format.

        Note: This endpoint is not currently available for Liquid/Elements-based chains.

        :param tx_id: String representing the transaction hash.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'tx/{tx_id}/merkleblock-proof', **kwargs)

    def get_merkle_proof(self, tx_id, **kwargs):
        r"""
        Returns a merkle inclusion proof for the transaction using
        `Electrum's blockchain.transaction.get_merkle <https://electrumx.readthedocs.io/en/latest/protocol-methods.html#blockchain-transaction-get-merkle>`_ format.

        :param tx_id: String representing the transaction hash.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'tx/{tx_id}/merkle-proof', **kwargs)

    def get_spending_status(self, tx_id, vout=None, **kwargs):
        r"""
        Returns the spending status of all transaction outputs.
        If `vout` is present, return the status of the transaction output located at that index.

        :param tx_id: String representing the transaction hash.
        :param vout: (Optional) Integer representing the index of the transaction output.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        path = f'tx/{tx_id}/outspend/{vout}' if vout is not None else f'tx/{tx_id}/outspends'
        return self.make_request('GET', path, **kwargs)

    def post(self, hex_tx, **kwargs):
        r"""
        Broadcast a raw transaction to the network.
        The transaction should be provided as hex in the request body.
        The `tx_id` will be returned as `data` on success.

        :param hex_tx: The transaction hex.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        return self.make_request('POST', 'tx', data=hex_tx, **kwargs)
