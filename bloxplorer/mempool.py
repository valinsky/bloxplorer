from bloxplorer.constants import http
from bloxplorer.utils import AsyncRequest, SyncRequest


class SyncMempool(SyncRequest):
    """
    Wrapper class around the Esplora Mempool endpoint.

    `Blockstream Esplora Mempool API Docs
    <https://github.com/Blockstream/esplora/blob/master/API.md#mempool>`_
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self, **kwargs):
        r"""
        Get mempool backlog statistics.

        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        return self.make_request(http.GET, 'mempool', **kwargs)

    def get_txids(self, **kwargs):
        r"""
        Get the full list of txids in the mempool as an array.
        The order of the txids is arbitrary and does not match bitcoind's.

        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        return self.make_request(http.GET, 'mempool/txids', **kwargs)

    def get_latest_txs(self, **kwargs):
        r"""
        Get a list of the last 10 transactions to enter the mempool.

        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        return self.make_request(http.GET, 'mempool/recent', **kwargs)


class AsyncMempool(AsyncRequest):

    async def get(self, **kwargs):
        return await self.make_request(http.GET, 'mempool', **kwargs)

    async def get_txids(self, **kwargs):
        return await self.make_request(http.GET, 'mempool/txids', **kwargs)

    async def get_latest_txs(self, **kwargs):
        return await self.make_request(http.GET, 'mempool/recent', **kwargs)
