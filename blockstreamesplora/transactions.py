from blockstreamesplora.utils import Request


class Transactions(Request):
    """
    Transactions API wrapper
    """

    def get_tx(self, tx_id):
        """
        Returns information about the transaction.
        """
        return self.get_from_path(f'tx/{tx_id}')

    def get_tx_status(self, tx_id):
        """
        Returns the transaction confirmation status
        """
        return self.get_from_path(f'tx/{tx_id}/status')

    def get_tx_raw_hex(self, tx_id):
        """
        Returns the raw transaction in hex.
        """
        return self.get_from_path(f'tx/{tx_id}/hex')

    def get_tx_merkle_proof(self, tx_id):
        """
        Returns a merkle inclusion proof for the transaction.
        """
        return self.get_from_path(f'tx/{tx_id}/merkle-proof')

    def get_tx_output_status(self, tx_id, vout):
        """
        Returns the spending status of a transaction output.
        """
        return self.get_from_path(f'tx/{tx_id}/outspend/{vout}')

    def get_tx_outspends(self, tx_id):
        """
        Returns the spending status of all transaction outputs.
        """
        return self.get_from_path(f'tx/{tx_id}/outspends')

    # def post_tx(data):
    #     """
    #     Broadcast a raw transaction to the network.
    #     The transaction should be provided as hex in the request body.
    #     The txid will be returned on success.
    #     """
        # url = urljoin(LIQUID_API_URL, 'tx')
        # response = requests.post(url, data=data)
        # return response
