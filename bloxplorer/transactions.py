from bloxplorer.utils import Request


class Transactions(Request):
    """
    Wrapper class around the Esplora Transactions endpoint.

    `Blockstream Esplora Transactions API Docs
    <https://github.com/Blockstream/esplora/blob/master/API.md#transactions>`_
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self, tx_id):
        """
        Returns information about the transaction.

        :param tx_id: String representing the transaction hash.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'tx/{tx_id}')

    def get_status(self, tx_id):
        """
        Returns the transaction confirmation status

        :param tx_id: String representing the transaction hash.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'tx/{tx_id}/status')

    def get_raw(self, tx_id):
        """
        Returns the raw transaction in hex.

        :param tx_id: String representing the transaction hash.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'tx/{tx_id}/hex')

    def get_merkle_proof(self, tx_id):
        """
        Returns a merkle inclusion proof for the transaction.

        :param tx_id: String representing the transaction hash.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'tx/{tx_id}/merkle-proof')

    def get_spending_status(self, tx_id, vout=None):
        """
        Returns the spending status of all transaction outputs.
        If `vout` is present, return the status of the transaction output located at that index.

        :param tx_id: String representing the transaction hash.
        :param vout: (Optional) Integer representing the index of the transaction output.

        :return: :class: `Response` object.
        """
        path = f'tx/{tx_id}/outspend/{vout}' if vout is not None else f'tx/{tx_id}/outspends'
        return self.make_request('GET', path)

    def post(self, hex_tx):
        """
        Broadcast a raw transaction to the network.
        The transaction should be provided as hex in the request body.
        The `tx_id` will be returned as `data` on success.

        :param hex_tx: The transaction hex.

        :return: :class: `Response` object.
        """
        return self.make_request('POST', 'tx', data=hex_tx)
