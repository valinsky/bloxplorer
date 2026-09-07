.. _mining:

Mining
======

The Mining class is available in all explorers when the Esplora server is started
with ``--enable-mining-rest``.

Sync Usage
**********

.. code-block:: python

    from bloxplorer import bitcoin_explorer as explorer

    result = explorer.mining.get_block_template()
    print(result.data)

Async Usage
***********

.. code-block:: python

    from bloxplorer import async_bitcoin_explorer as async_explorer

    result = await async_explorer.mining.get_block_template()
    print(result.data)

Result
******

Both usages return the daemon's ``getblocktemplate`` response. Example output:

.. code-block:: python

    """
    {
        'version': 536870912,
        'rules': ['segwit'],
        'vbavailable': {},
        'vbrequired': 0,
        'previousblockhash': '000000000000000000010b6ed9d2333c0797ab02f244ad2adc8734fdf6cd03de',
        'transactions': [],
        'coinbaseaux': {'flags': '03'},
        'coinbasevalue': 312500000,
        'target': '0000000000000000000342db0000000000000000000000000000000000000000',
        'mintime': 1762016765,
        'mutable': ['time', 'transactions', 'prevblock'],
        'noncerange': '00000000ffffffff',
        'sigoplimit': 80000,
        'sizelimit': 4000000,
        'weightlimit': 4000000,
        'curtime': 1762017000,
        'bits': '170342db',
        'height': 921776
    }
    """

Available methods
*****************

.. autoclass:: bloxplorer.mining.SyncMining
    :members:
