from bloxplorer.utils import Request


class Blocks(Request):
    """
    Wrapper class around the Esplora Blocks endpoint.

    `Blockstream Esplora Blocks API Docs
    <https://github.com/Blockstream/esplora/blob/master/API.md#blocks>`_
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.cache = {}

    def get(self, hash, **kwargs):
        r"""
        Returns information about a block.
        The response from this endpoint can be cached indefinitely.

        :param hash: String representing the block hash.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'block/{hash}', **kwargs)

    def get_status(self, hash, **kwargs):
        r"""
        Returns information about the block status.
        The response from this endpoint can be cached indefinitely.

        :param hash: String representing the block hash.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'block/{hash}/status', **kwargs)

    def get_txs(self, hash, start_index=None, **kwargs):
        r"""
        Returns a list of transactions in the block (up to 25 transactions beginning at start_index).
        Transactions returned here do not have the status field, since all the transactions share the
        same block and confirmation status.
        The response from this endpoint can be cached indefinitely.

        :param hash: String representing the block hash.
        :param start_index: (Optional) Integer representing the transaction start index.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        path = f'block/{hash}/txs'
        if start_index is not None:
            path = f'{path}/{start_index}'
        return self.make_request('GET', path, **kwargs)

    def get_txids(self, hash, index=None, **kwargs):
        r"""
        Returns a list of all txids in the block.
        If `index` is present, return the transaction at index `index` within the specified block.
        The response from this endpoint can be cached indefinitely.

        :param hash: String representing the block hash.
        :param index: (Optional) Integer representing the index within a block.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        path = f'block/{hash}/txid/{index}' if index is not None else f'block/{hash}/txids'
        return self.make_request('GET', path, **kwargs)

    def get_height(self, height, **kwargs):
        r"""
        Returns the hash of the block currently at `height`.

        :param height: Integer representing the block height.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'block-height/{height}', **kwargs)

    def get_blocks(self, start_height=None, **kwargs):
        r"""
        Returns the 10 newest blocks starting at the tip or at `start_height` if specified.

        :param start_height: (Optional) Integer representing the block height.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        path = f'blocks'
        if start_height is not None:
            path = f'{path}/{start_height}'
        return self.make_request('GET', path, **kwargs)

    def get_last_height(self, **kwargs):
        r"""
        Returns the height of the last block.

        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', 'blocks/tip/height', **kwargs)

    def get_last_hash(self, **kwargs):
        r"""
        Returns the hash of the last block.

        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', 'blocks/tip/hash', **kwargs)
