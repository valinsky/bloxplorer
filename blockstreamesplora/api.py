from blockstreamesplora import transactions, addresses


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

def get_address(address):
    return addresses.get(address)

def get_scripthash(hash):
    return addresses.get_scripthash(hash)

def get_address_tx_history(address, last_seen_txid=None):
    return addresses.get_tx_history(address, last_seen_txid)

def get_scripthash_tx_history(hash, last_seen_txid=None):
    return addresses.get_scripthash_tx_history(hash, last_seen_txid)

def get_address_unconfirmed_tx_history(address):
    return addresses.get_unconfirmed_tx_history(address)

def get_scripthash_unconfirmed_tx_history(hash):
    return addresses.get_scripthash_unconfirmed_tx_history(hash)

def get_address_utxo(address):
    return addresses.get_utxo(address)

def get_scripthash_utxo(hash):
    return addresses.get_scripthash_utxo(hash)


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