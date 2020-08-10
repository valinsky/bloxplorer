from bloxplorer.utils import Request


class IssuedAssets(Request):
    """
    Wrapper class around the Esplora Issued Assets endpoint.
    Only for Elements / Liquid.

    `Blockstream Esplora Issued Assets API Docs
    <https://github.com/Blockstream/esplora/blob/master/API.md#assets-elementsliquid-only>`_
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self, asset_id, **kwargs):
        r"""
        Get information about an issued asset.

        :param asset_id: String representing the issued asset hash.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'asset/{asset_id}', **kwargs)

    def get_txs(self, asset_id, **kwargs):
        r"""
        Returns the list of (re)issuance and burn transactions associated with this asset id.
        Does not include regular transactions transferring this asset.

        :param asset_id: String representing the issued asset hash.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'asset/{asset_id}/txs', **kwargs)

    def get_mempool(self, asset_id, **kwargs):
        r"""
        Returns the list of (re)issuance and burn transactions associated with this asset id.
        Does not include regular transactions transferring this asset.

        :param asset_id: String representing the issued asset hash.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'asset/{asset_id}/txs/mempool', **kwargs)

    def get_chain(self, asset_id, last_seen=None, **kwargs):
        r"""
        Returns the list of (re)issuance and burn transactions associated with this asset id.
        Does not include regular transactions transferring this asset.

        :param asset_id: String representing the issued asset hash.
        :param last_seen:
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        path = f'asset/{asset_id}/txs/chain'
        if last_seen:
            path = f'{path}/{last_seen}'
        return self.make_request('GET', path, **kwargs)

    def get_supply(self, asset_id, decimal=False, **kwargs):
        r"""
        Get the current total supply of the specified asset.
        Not available for assets with blinded issuances.

        :param asset_id: String representing the issued asset hash.
        :param decimal: Boolean that returns the supply as decimal if set.
                        Return in base units if not set (default).
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        path = f'asset/{asset_id}/supply'
        if decimal:
            path = f'{path}/decimal'
        return self.make_request('GET', path, **kwargs)
