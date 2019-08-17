from bloxplorer.utils import Request


class Addresses(Request):
    """
    Wrapper class around the Esplora Addresses endpoint.

    `Blockstream Esplora Addresses API Docs
    <https://github.com/Blockstream/esplora/blob/master/API.md#addresses>`_
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self, address):
        """
        Get information about an address.

        :param address: String representing the address.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'address/{address}')

    def get_scripthash(self, hash):
        """
        Get information about a scripthash.

        :param hash: String representing the scripthash.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'scripthash/{hash}')

    def get_tx_history(self, address):
        """
        Get transaction history for the specified address, sorted with newest first.
        Returns up to 50 unconfirmed transactions plus the first 25 confirmed transactions.
        You can request more confirmed transactions using `last_seen_txid` inside
        `get_confirmed_tx_history` method.

        :param address: String representing the address.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'address/{address}/txs')

    def get_scripthash_tx_history(self, hash):
        """
        Get transaction history for the specified scripthash, sorted with newest first.
        Returns up to 50 mempool transactions plus the first 25 confirmed transactions.
        You can request more confirmed transactions using `last_seen_txid` inside
        `get_confirmed_scripthash_tx_history` method.

        :param hash: String representing the scripthash.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'scripthash/{hash}/txs')

    def get_confirmed_tx_history(self, address, last_seen_txid=None):
        """
        Get confirmed transaction history for the specified address, sorted with newest first.
        Returns 25 transactions per request.
        More can be requested by specifying the `last_seen_txid` from `get_tx_history` response.

        :param address: String representing the address.
        :param last_seen_txid: (Optional) String representing the transaction hash.

        :return: :class: `Response` object.
        """
        path = f'address/{address}/txs/chain'
        if last_seen_txid is not None:
            path += f'/{last_seen_txid}'
        return self.make_request('GET', path)

    def get_confirmed_scripthash_tx_history(self, hash, last_seen_txid=None):
        """
        Get confirmed transaction history for the specified scripthash, sorted with newest first.
        Returns 25 transactions per request.
        More can be requested by specifying the `last_seen_txid` from
        `get_scripthash_tx_history` response.

        :param hash: String representing the scripthash.
        :param last_seen_txid: (Optional) String representing the transaction hash.

        :return: :class: `Response` object.
        """
        path = f'scripthash/{hash}/txs/chain'
        if last_seen_txid is not None:
            path += f'/{last_seen_txid}'
        return self.make_request('GET', path)

    def get_unconfirmed_tx_history(self, address):
        """
        Get unconfirmed transaction history for the specified address.
        Returns up to 50 transactions.

        :param address: String representing the address.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'address/{address}/txs/mempool')

    def get_unconfirmed_scripthash_tx_history(self, hash):
        """
        Get unconfirmed transaction history for the specified scripthash.
        Returns up to 50 transactions.

        :param hash: String representing the scripthash.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'scripthash/{hash}/txs/mempool')

    def get_utxo(self, address):
        """
        Get the list of unspent transaction outputs associated with the address.

        :param address: String representing the address.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'address/{address}/utxo')

    def get_scripthash_utxo(self, hash):
        """
        Get the list of unspent transaction outputs associated with the scripthash.

        :param hash: String representing the scripthash.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'scripthash/{hash}/utxo')
