from blockstreamesplora.utils import Request


class Addresses(Request):
    """
    Addresses API Wrapper
    """

    def get_address(self, address):
        """
        Get information about an address.
        """
        return self.get_from_path(f'address/{address}')

    def get_scripthash(self, hash):
        """
        Get information about a scripthash.
        """
        return self.get_from_path(f'scripthash/{address}')

    def get_address_tx_history(self, address, last_seen_txid=None):
        """
        Get transaction history for the specified address/scripthash, sorted with newest first.

        Returns up to 50 mempool transactions plus the first 25 confirmed transactions.
        You can request more confirmed transactions using `last_seen_txid`.
        """
        # need a check on `last_seen_txid`
        path = f'address/{address}/txs'
        if last_seen_txid:
            path += '/chain/{last_seen_txid}'
        return self.get_from_path(path)

    def get_scripthash_tx_history(self, hash, last_seen_txid=None):
        """
        Get transaction history for the specified scripthash, sorted with newest first.

        Returns up to 50 mempool transactions plus the first 25 confirmed transactions.
        You can request more confirmed transactions using `last_seen_txid`.
        """
        # need a check on `last_seen_txid`
        path = f'scripthash/{hash}/txs'
        if last_seen_txid:
            path += '/chain/{last_seen_txid}'
        return self.get_from_path(path)

    def get_address_unconfirmed_tx_history(self, address):
        """
        Get unconfirmed transaction history for the specified address.
        Returns up to 50 transactions (no paging).
        """
        return self.get_from_path(f'address/{address}/txs/mempool')

    def get_scripthash_unconfirmed_tx_history(self, hash):
        """
        Get unconfirmed transaction history for the specified scripthash.
        Returns up to 50 transactions (no paging).
        """
        return self.get_from_path(f'scripthash/{hash}/txs/mempool')

    def get_address_utxo(self, address):
        """
        Get the list of unspent transaction outputs associated with the address.
        """
        return self.get_from_path(f'address/{address}/utxo')

    def get_scripthash_utxo(self, hash):
        """
        Get the list of unspent transaction outputs associated with the scripthash.
        """
        return self.get_from_path(f'scripthash/{hash}/utxo')
