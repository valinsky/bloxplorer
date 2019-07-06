from blockstreamesplora.utils import get_from_path


def get(hash):
    """
    Returns information about a block.
    The response from this endpoint can be cached indefinitely.
    """
    return get_from_path(f'block/{hash}')

def get_status(hash):
    """
    Returns information about the block status.
    The response from this endpoint can be cached indefinitely.
    """
    return get_from_path(f'block/{hash}/status')

def get_txs(hash, start_index=None):
    """
    Returns a list of transactions in the block (up to 25 transactions beginning at start_index).
    Transactions returned here do not have the status field, since all the transactions share the
    same block and confirmation status.
    The response from this endpoint can be cached indefinitely.
    """
    path = f'block/{hash}/txs'
    if start_index:
        path += f'/{start_index}'
    return get_from_path(path)

def get_txids(hash):
    """
    Returns a list of all txids in the block.
    The response from this endpoint can be cached indefinitely.
    """
    return get_from_path(f'block/{hash}/txids')

def get_height(height):
    """
    Returns the hash of the block currently at height.
    """
    return get_from_path(f'block-height/{height}')

def get_blocks(start_height=None):
    """
    Returns the 10 newest blocks starting at the tip or at `start_height` if specified.
    """
    path = f'/block'
    if start_height:
        path += f'/{start_height}'
    return get_from_path(path)

def get_last_block_height():
    """
    Returns the height of the last block.
    """
    return get_from_path('blocks/tip/height')

def get_last_block_hash():
    """
    Returns the hash of the last block.
    """
    return get_from_path('blocks/tip/hash')
