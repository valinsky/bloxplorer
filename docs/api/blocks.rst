.. _blocks:

Blocks
======

The Blocks class is available in all explorers.

Sync Usage
**********

.. code-block:: python

    from bloxplorer import bitcoin_explorer as explorer

    result = explorer.blocks.get('000000000000000000010b6ed9d2333c0797ab02f244ad2adc8734fdf6cd03de')
    print(result.data)

Async Usage
***********

.. code-block:: python

    from bloxplorer import async_bitcoin_explorer as async_explorer

    result = await async_explorer.blocks.get('000000000000000000010b6ed9d2333c0797ab02f244ad2adc8734fdf6cd03de')
    print(result.data)

Result
******

Both usages will output the same result data. Example output:

.. code-block:: python

    """
    {
        'id': '000000000000000000010b6ed9d2333c0797ab02f244ad2adc8734fdf6cd03de',
        'height': 921775,
        'version': 717307904,
        'timestamp': 1762016765,
        'tx_count': 2822,
        'size': 1484850,
        'weight': 3993429,
        'merkle_root': 'a1f10dc62eb61cd5d15ebf6fa833b6176faebca5930a1dd41699fd064650a6d8',
        'previousblockhash': '00000000000000000000610ab96dec47a277be98d3173857597e0d266249da7a',
        'mediantime': 1762011777,
        'nonce': 2992019156,
        'bits': 385994235,
        'difficulty': 155973032196071.94
    }
    """

Available methods
*****************

.. autoclass:: bloxplorer.blocks.SyncBlocks
    :members:
