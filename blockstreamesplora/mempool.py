from blockstreamesplora.utils import get_from_path


def get():
    """
    Get mempool backlog statistics.
    """
    return get_from_path('mempool')

def get_txids():
    """
    Get the full list of txids in the mempool as an array.
    The order of the txids is arbitrary and does not match bitcoind's.
    """
    return get_from_path('mempool/txids')

def get_latest_txs():
    """
    Get a list of the last 10 transactions to enter the mempool.
    """
    return get_from_path('mempool/recent')
