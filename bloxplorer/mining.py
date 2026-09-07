from bloxplorer.constants import http
from bloxplorer.utils import AsyncRequest, SyncRequest


class SyncMining(SyncRequest):
    """
    Wrapper class around the Esplora Mining endpoint.

    `Blockstream Esplora Mining API Docs
    <https://github.com/Blockstream/esplora/blob/master/API.md#mining>`_
    """

    def get_block_template(self, **kwargs):
        r"""
        Returns the daemon's ``getblocktemplate`` response for mining.

        This endpoint is available only when electrs is started with
        ``--enable-mining-rest``.

        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        return self.make_request(http.GET, 'block-template', **kwargs)


class AsyncMining(AsyncRequest):

    async def get_block_template(self, **kwargs):
        return await self.make_request(http.GET, 'block-template', **kwargs)
