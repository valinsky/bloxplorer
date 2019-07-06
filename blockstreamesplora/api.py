from blockstreamesplora import transactions, addresses, blocks, mempool, fees


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

def get_block(hash):
    return blocks.get(hash)

def get_block_status(hash):
    return blocks.get_status(hash)

def get_block_txs(hash, start_index=None):
    return blocks.get_txs(hash, start_index)

def get_block_txids(hash):
    return blocks.get_txids(hash)

def get_block_height(height):
    return blocks.get_height(height)

def get_blocks(start_height=None):
    return blocks.get_blocks(start_height)

def get_last_block_height():
    return blocks.get_last_block_height()

def get_last_block_hash():
    return blocks.get_last_block_hash()


"""
Mempool API Wrapper
"""

def get_mempool():
    return mempool.get()

def get_mempool_txids():
    return mempool.get_txids()

def get_mempool_latest_txs():
    return mempool.get_latest_txs()


"""
Fee estimates API Wrapper
"""
def get_fee_estimates():
    fees.get()
