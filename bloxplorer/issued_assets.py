from bloxplorer.utils import Request


class IssuedAssets(Request):
    """
    Wrapper class around the Esplora Issued Assets endpoint.
    Only for Elements / Liquid.

    `Blockstream Esplora Issued Assets API Docs
    <https://github.com/Blockstream/esplora/blob/master/API.md#issued-assets-elementsliquid-only>`_
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self, asset_id):
        """
        Get information about an issued assets.

        :param asset_id: String representing the issued asset hash.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'asset/{asset_id}')

    def get_txs(self, asset_id):
        """
        Returns the list of (re)issuance and burn transactions associated with this asset id.
        Does not include regular transactions transferring this asset.

        :param asset_id: String representing the issued asset hash.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'asset/{asset_id}/txs')

    def get_mempool(self, asset_id):
        """
        Returns the list of (re)issuance and burn transactions associated with this asset id.
        Does not include regular transactions transferring this asset.

        :param asset_id: String representing the issued asset hash.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'asset/{asset_id}/txs/mempool')

    def get_chain(self, asset_id, last_seen=None):
        """
        Returns the list of (re)issuance and burn transactions associated with this asset id.
        Does not include regular transactions transferring this asset.

        :param asset_id: String representing the issued asset hash.
        :param last_seen: TODO

        :return: :class: `Response` object.
        """
        path = f'asset/{asset_id}/txs/chain'
        if last_seen:
            path += f'/{last_seen}'
        return self.make_request('GET', path)
