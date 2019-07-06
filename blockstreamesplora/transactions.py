from blockstreamesplora.utils import get_from_path


def get(tx_id):
    """
    Returns information about the transaction.
    """
    return get_from_path(f'tx/{tx_id}')

def get_status(tx_id):
    """
    Returns the transaction confirmation status
    """
    return get_from_path(f'tx/{tx_id}/status')

def get_raw(tx_id):
    """
    Returns the raw transaction in hex.
    """
    return get_from_path(f'tx/{tx_id}/hex')

def get_merkle_proof(tx_id):
    """
    Returns a merkle inclusion proof for the transaction.
    """
    return get_from_path(f'tx/{tx_id}/merkle-proof')

def get_output_status(tx_id, vout):
    """
    Returns the spending status of a transaction output.
    """
    return get_from_path(f'tx/{tx_id}/outspend/{vout}')

def get_outspends(tx_id):
    """
    Returns the spending status of all transaction outputs.
    """
    return get_from_path(f'tx/{tx_id}/outspends')

# def post_tx(data):
#     """
#     Broadcast a raw transaction to the network.
#     The transaction should be provided as hex in the request body.
#     The txid will be returned on success.
#     """
    # url = urljoin(LIQUID_API_URL, 'tx')
    # response = requests.post(url, data=data)
    # return response
