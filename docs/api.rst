.. _api:

API Documentation
=================

The `Blockstream Esplora API <https://github.com/Blockstream/esplora/blob/master/API.md>`_ exposes
multiple endpoints associated with the following resources:
`Transactions <https://github.com/Blockstream/esplora/blob/master/API.md#transactions>`_,
`Addresses <https://github.com/Blockstream/esplora/blob/master/API.md#addresses>`_,
`Blocks <https://github.com/Blockstream/esplora/blob/master/API.md#blocks>`_,
`Mempool <https://github.com/Blockstream/esplora/blob/master/API.md#mempool>`_,
`Fee estimates <https://github.com/Blockstream/esplora/blob/master/API.md#fee-estimates>`_ and
`Issued assets <https://github.com/Blockstream/esplora/blob/master/API.md#issued-assets-elementsliquid-only>`_.

Bloxplorer is a Python wrapper around these endpoints.

The explorers are instantiated with the following endpoint urls:

* Bitcoin Explorer: https://blockstream.info/api/
* Bitcoin Testnet Explorer: https://blockstream.info/testnet/api/
* Bitcoin Signet Explorer: https://blockstream.info/signet/api/
* Liquid Explorer: https://blockstream.info/liquid/api/

After you import an explorer, you can use its methods by following this notation:

    >>> explorer.resource.method(*args, **kwargs)

Example:

    >>> bitcoin_explorer.blocks.get_blocks(start_height='587840')

All the available resource methods are documented below:

.. toctree::
    :maxdepth: 2

    api/addresses
    api/blocks
    api/transactions
    api/mempool
    api/fee_estimates
    api/issued_assets
