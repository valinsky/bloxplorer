.. _transactions:

Transactions
============

The Transactions class is available in all explorers.

Sync Usage
**********

.. code-block:: python

    from bloxplorer import bitcoin_explorer as explorer

    result = explorer.tx.get('f29e151e71db58ade22be066afafdc59ed7df8195e3944a5e577b275dc37bf94')
    print(result.data)

Async Usage
***********

.. code-block:: python

    from bloxplorer import async_bitcoin_explorer as async_explorer

    result = await async_explorer.tx.get('f29e151e71db58ade22be066afafdc59ed7df8195e3944a5e577b275dc37bf94')
    print(result.data)

Result
******

Both usages will output the same result data. Example output:

.. code-block:: python

    """
    {
        'txid': '42d7717a80ade0b1f12481a392def5521254f2da243f4e88a850aa7e3fc3c017',
        'version': 1,
        'locktime': 0,
        'vin': [
            {
                'txid': '6d84e0715d6d729c891bf77bf7b758c329b415c5faff423ba95b6f5ba7c8449c',
                'vout': 0,
                'prevout': {
                    'scriptpubkey': '001440c6676b80f6df036c18af0678b2bcbba029407f',
                    'scriptpubkey_asm': 'OP_0 OP_PUSHBYTES_20 40c6676b80f6df036c18af0678b2bcbba029407f',
                    'scriptpubkey_type': 'v0_p2wpkh',
                    'scriptpubkey_address': 'bc1qgrrxw6uq7m0sxmqc4ur83v4uhwszjsrlpe9hwm',
                    'value': 473862
                },
            'scriptsig': '',
            'scriptsig_asm': '',
            'witness': [
                '3045022100a4f3567101168da5b96d6b9f89a206ef297eb87e993da0c2563b50fce42abfd70220655c90f59fe0b9b5db331fe327ec466d7e97de5ca9b97b4e8fc8330f003c4fe901',
                '036081cb5819b0e98d9d28319d83e6e67de21a529202e9b6465b7992053b422521'
            ],
            'is_coinbase': False,
            'sequence': 4294967295
        }
    ],
    'vout': [
        {
            'scriptpubkey': '0014ca95888d9d192b22b0bdc8d8755412d24c30f02d',
            'scriptpubkey_asm': 'OP_0 OP_PUSHBYTES_20 ca95888d9d192b22b0bdc8d8755412d24c30f02d',
            'scriptpubkey_type': 'v0_p2wpkh',
            'scriptpubkey_address': 'bc1qe22c3rvary4j9v9aerv824qj6fxrpupdlyqp4r',
            'value': 106489
        },
        {
            'scriptpubkey': '0014173215f2ff25ec479498ef2d6ad60419837b0234',
            'scriptpubkey_asm': 'OP_0 OP_PUSHBYTES_20 173215f2ff25ec479498ef2d6ad60419837b0234',
            'scriptpubkey_type': 'v0_p2wpkh',
            'scriptpubkey_address': 'bc1qzueptuhlyhky09ycaukk44syrxphkq35pt65w5',
            'value': 364976
        }
    ],
    'size': 223,
    'weight': 562,
    'fee': 2397,
    'status': {
        'confirmed': True,
        'block_height': 921775,
        'block_hash': '000000000000000000010b6ed9d2333c0797ab02f244ad2adc8734fdf6cd03de',
        'block_time': 1762016765
    }}
    """

Available methods
*****************

.. autoclass:: bloxplorer.transactions.SyncTransactions
    :members:
