from blockstreamesplora import transactions

"""
Transactions API wrapper
"""

def get_tx(tx_id):
    return transactions.get(tx_id)

def get_tx_status(tx_id):
    return transactions.get_status(tx_id)

def get_tx_raw_hex(tx_id):
    return transactions.get_raw(tx_id)

def get_tx_merkle_proof(tx_id):
    return transactions.get_merkle_proof(tx_id)

def get_tx_output_status(tx_id, vout):
    return transactions.get_output_status(tx_id, vout)

def get_tx_outspends(tx_id):
    return transactions.get_outspends(tx_id)

def post_tx(data):
    """
    Broadcast a raw transaction to the network.
    The transaction should be provided as hex in the request body.
    The txid will be returned on success.
    """
    # url = urljoin(LIQUID_API_URL, 'tx')
    # response = requests.post(url, data=data)
    # return response

"""
Addresses API Wrapper
"""
# TODO

"""
Block API Wrapper
"""
# TODO

"""
Mempool API Wrapper
"""
# TODO

"""
Fee estimates API Wrapper
"""
# TODO