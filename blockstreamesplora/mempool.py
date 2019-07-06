from blockstreamesplora.utils import Request


class Mempool(Request):
    """
    Mempool API Wrapper
    """

    def get_mempool(self):
        """
        Get mempool backlog statistics.
        """
        return self.get_from_path('mempool')

    def get_mempool_txids(self):
        """
        Get the full list of txids in the mempool as an array.
        The order of the txids is arbitrary and does not match bitcoind's.
        """
        return self.get_from_path('mempool/txids')

    def get_mempool_latest_txs(self):
        """
        Get a list of the last 10 transactions to enter the mempool.
        """
        return self.get_from_path('mempool/recent')
