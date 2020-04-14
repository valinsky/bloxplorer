from bloxplorer.utils import Request


class Addresses(Request):
    """
    Wrapper class around the Esplora Addresses endpoint.

    `Blockstream Esplora Addresses API Docs
    <https://github.com/Blockstream/esplora/blob/master/API.md#addresses>`_
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self, address, **kwargs):
        r"""
        Get information about an address.

        :param address: String representing the address.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'address/{address}', **kwargs)

    def get_scripthash(self, hash, **kwargs):
        r"""
        Get information about a scripthash.

        :param hash: String representing the scripthash.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'scripthash/{hash}', **kwargs)

    def get_tx_history(self, address, **kwargs):
        r"""
        Get transaction history for the specified address, sorted with newest first.
        Returns up to 50 unconfirmed transactions plus the first 25 confirmed transactions.
        You can request more confirmed transactions using `last_seen_txid` inside
        `get_confirmed_tx_history` method.

        :param address: String representing the address.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'address/{address}/txs', **kwargs)

    def get_scripthash_tx_history(self, hash, **kwargs):
        r"""
        Get transaction history for the specified scripthash, sorted with newest first.
        Returns up to 50 mempool transactions plus the first 25 confirmed transactions.
        You can request more confirmed transactions using `last_seen_txid` inside
        `get_confirmed_scripthash_tx_history` method.

        :param hash: String representing the scripthash.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'scripthash/{hash}/txs', **kwargs)

    def get_confirmed_tx_history(self, address, last_seen_txid=None, **kwargs):
        r"""
        Get confirmed transaction history for the specified address, sorted with newest first.
        Returns 25 transactions per request.
        More can be requested by specifying the `last_seen_txid` from `get_tx_history` response.

        :param address: String representing the address.
        :param last_seen_txid: (Optional) String representing the transaction hash.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        path = f'address/{address}/txs/chain'
        if last_seen_txid is not None:
            path += f'/{last_seen_txid}'
        return self.make_request('GET', path, **kwargs)

    def get_confirmed_scripthash_tx_history(self, hash, last_seen_txid=None, **kwargs):
        r"""
        Get confirmed transaction history for the specified scripthash, sorted with newest first.
        Returns 25 transactions per request.
        More can be requested by specifying the `last_seen_txid` from
        `get_scripthash_tx_history` response.

        :param hash: String representing the scripthash.
        :param last_seen_txid: (Optional) String representing the transaction hash.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        path = f'scripthash/{hash}/txs/chain'
        if last_seen_txid is not None:
            path += f'/{last_seen_txid}'
        return self.make_request('GET', path, **kwargs)

    def get_unconfirmed_tx_history(self, address, **kwargs):
        r"""
        Get unconfirmed transaction history for the specified address.
        Returns up to 50 transactions.

        :param address: String representing the address.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'address/{address}/txs/mempool', **kwargs)

    def get_unconfirmed_scripthash_tx_history(self, hash, **kwargs):
        r"""
        Get unconfirmed transaction history for the specified scripthash.
        Returns up to 50 transactions.

        :param hash: String representing the scripthash.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'scripthash/{hash}/txs/mempool', **kwargs)

    def get_utxo(self, address, **kwargs):
        r"""
        Get the list of unspent transaction outputs associated with the address.

        :param address: String representing the address.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'address/{address}/utxo', **kwargs)

    def get_scripthash_utxo(self, hash, **kwargs):
        r"""
        Get the list of unspent transaction outputs associated with the scripthash.

        :param hash: String representing the scripthash.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'scripthash/{hash}/utxo', **kwargs)

    def get_address_prefix(self, prefix, **kwargs):
        r"""
        Search for addresses beginning with :prefix.
        Returns an array with up to 10 results.

        :param prefix: String representing the prefix the address begins with.
        :param \*\*kwargs: (Optional) Arguments that `Requests` takes.

        :return: :class: `Response` object.
        """
        return self.make_request('GET', f'address-prefix/{prefix}', **kwargs)

    @staticmethod
    def get_address_type(address):
        """
        Get the Bitcoin address type.
        Not available for Liquid.

        :param address: The alphanumeric Bitcoin address

        :return: String representing the address type (P2PKH, P2SH, etc.)
        """
        pass
