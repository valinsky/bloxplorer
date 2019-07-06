from blockstreamesplora.utils import Request


class Blocks(Request):
    """
    Block API Wrapper
    """

    def get_block(self, hash):
        """
        Returns information about a block.
        The response from this endpoint can be cached indefinitely.
        """
        return self.get_from_path(f'block/{hash}')

    def get_block_status(self, hash):
        """
        Returns information about the block status.
        The response from this endpoint can be cached indefinitely.
        """
        return self.get_from_path(f'block/{hash}/status')

    def get_block_txs(self, hash, start_index=None):
        """
        Returns a list of transactions in the block (up to 25 transactions beginning at start_index).
        Transactions returned here do not have the status field, since all the transactions share the
        same block and confirmation status.
        The response from this endpoint can be cached indefinitely.
        """
        path = f'block/{hash}/txs'
        if start_index:
            path += f'/{start_index}'
        return self.get_from_path(path)

    def get_block_txids(self, hash):
        """
        Returns a list of all txids in the block.
        The response from this endpoint can be cached indefinitely.
        """
        return self.get_from_path(f'block/{hash}/txids')

    def get_block_height(self, height):
        """
        Returns the hash of the block currently at height.
        """
        return self.get_from_path(f'block-height/{height}')

    def get_blocks(self, start_height=None):
        """
        Returns the 10 newest blocks starting at the tip or at `start_height` if specified.
        """
        path = f'/block'
        if start_height:
            path += f'/{start_height}'
        return self.get_from_path(path)

    def get_last_block_height(self):
        """
        Returns the height of the last block.
        """
        return self.get_from_path('blocks/tip/height')

    def get_last_block_hash(self):
        """
        Returns the hash of the last block.
        """
        return self.get_from_path('blocks/tip/hash')
