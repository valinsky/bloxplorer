.. _transactions:

Transactions
============

The Transactions class is available in all explorers.

Usage
*****

.. code-block:: python

    from bloxplorer import bitcoin_testnet_explorer as explorer

    result = explorer.tx.get('6d0139c3d0f529dda57496f1eabf0b32c9296c93b49b7a4965fa5ad91be4f216')
    print(result.data)

    """
    {
        'txid': '6d0139c3d0f529dda57496f1eabf0b32c9296c93b49b7a4965fa5ad91be4f216',
        'version': 2,
        'locktime': 0,
        'vin': [
            {
            'txid': '0000000000000000000000000000000000000000000000000000000000000000',
            'vout': 4294967295,
            'prevout': null,
            'scriptsig': '03cffd170454c6445d44434578706c6f726174696f6e09000fdddd13000000000000',
            'scriptsig_asm': 'OP_PUSHBYTES_3 cffd17 OP_PUSHBYTES_4 54c6445d OP_PUSHBYTES_68 <push past end>',
            'witness': [
                '0000000000000000000000000000000000000000000000000000000000000000'
            ],
            'is_coinbase': true,
            'sequence': 4294967295
            }
        ],
        'vout': [
            {
            'scriptpubkey': 'a914e0725ef08b0046fd2df3c58d5fefc5580e1f59de87',
            'scriptpubkey_asm': 'OP_HASH160 OP_PUSHBYTES_20 e0725ef08b0046fd2df3c58d5fefc5580e1f59de OP_EQUAL',
            'scriptpubkey_type': 'p2sh',
            'scriptpubkey_address': '2NDhzMt2D9ZxXapbuq567WGeWP7NuDN81cg',
            'value': 39218600
            },
            {
            'scriptpubkey': '6a24aa21a9ede772884776c199b25a5019a413713737c23c0d3e3d71e75aac7ac43b3df059ec',
            'scriptpubkey_asm': 'OP_RETURN OP_PUSHBYTES_36 aa21a9ede772884776c199b25a5019a413713737c23c0d3e3d71e75aac7ac43b3df059ec',
            'scriptpubkey_type': 'op_return',
            'value': 0
            }
        ],
        'size': 200,
        'weight': 692,
        'status': {
            'confirmed': true,
            'block_height': 1572303,
            'block_hash': '00000000000001decd01ced9b0b98f15ffb600f6abd27e0634809a90268b3765',
            'block_time': 1564788341
        }
        }
    """

.. autoclass:: bloxplorer.transactions.Transactions
    :members:
