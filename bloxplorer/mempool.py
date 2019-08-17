from bloxplorer.utils import Request


class Mempool(Request):
    """
    Wrapper class around the Esplora Mempool endpoint.

    `Blockstream Esplora Mempool API Docs
    <https://github.com/Blockstream/esplora/blob/master/API.md#mempool>`_
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self):
        """
        Get mempool backlog statistics.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', 'mempool')

    def get_txids(self):
        """
        Get the full list of txids in the mempool as an array.
        The order of the txids is arbitrary and does not match bitcoind's.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', 'mempool/txids')

    def get_latest_txs(self):
        """
        Get a list of the last 10 transactions to enter the mempool.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', 'mempool/recent')
