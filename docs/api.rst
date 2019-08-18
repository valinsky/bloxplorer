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

The Bloxplorer package contains wrapper classes around each of these resources.
Every class provides all the necessary methods needed to interact with the specific resource in a 
simple and straightfoward manner. The Issued Assets property is present only in the Liquid Explorer.

The explorers have a set of properties composed of the instantiation of the wrapper classes with 
the specific base url as follows:

| Bitcoin Explorer: https://blockstream.info/api/
| Liquid Explorer: https://blockstream.info/liquid/api/
| Bitcoin Testnet Explorer: https://blockstream.info/testnet/api/

After you import an explorer, you can use the API by following this notation:

    >>> explorer.property.method(*args, **kwargs)

Example:

    >>> bitcoin_explorer.blocks.get_blocks(start_height='587840')

The set of properties available are : *addr*, *tx*, *blocks*, *fees*, *mempool*, *assets*

All the available resource methods are documented below:

.. toctree::
    :maxdepth: 2

    api/addresses
    api/blocks
    api/transactions
    api/mempool
    api/fee_estimates
    api/issued_assets

