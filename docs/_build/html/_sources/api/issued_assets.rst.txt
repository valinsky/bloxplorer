.. _issues_assets:

Issued Assets
=============

The Issued Assets class is available only for the Elements / Liquid explorer.

Usage
*****

.. code-block:: python

    from bloxplorer import liquid_explorer as explorer

    result = explorer.assets.get('aa775044c32a7df391902b3659f46dfe004ccb2644ce2ddc7dba31e889391caf')
    print(result.data)

    """
    {
        'asset_id': 'aa775044c32a7df391902b3659f46dfe004ccb2644ce2ddc7dba31e889391caf',
        'issuance_txin': {
            'txid': '421dd5195c9f36bd56a79e3b0581620b11804ec9fbc9d03b36102c27781536c8',
            'vin': 0
        },
        'issuance_prevout': {
            'txid': '7ead93672f90b8eb6ccdc73ffe0cf0e1381023bd72ecdcbc73a33e9e6e9fcc1f',
            'vout': 0
        },
        'reissuance_token': 'fe9ae6c5dad9de797edeb0327f637920798134c428c3ac781f5267d063e34eca',
        'contract_hash': 'ea0777a80ef195009d487ae3eb49bb6d82fbc8d8064c81d7cfb515a3d3fe5438',
        'status': {
            'confirmed': True,
            'block_height': 470055,
            'block_hash': '7596b3dcfae149c29f558af284fb89e8fb635541db700aa22634a5f03a5623ce',
            'block_time': 1568422618
        },
        'chain_stats': {
            'tx_count': 1,
            'issuance_count': 1,
            'issued_amount': 1000000,
            'burned_amount': 0,
            'has_blinded_issuances': False,
            'reissuance_tokens': 5,
            'burned_reissuance_tokens': 0
        },
        'mempool_stats': {
            'tx_count': 0,
            'issuance_count': 0,
            'issued_amount': 0,
            'burned_amount': 0,
            'has_blinded_issuances': False,
            'reissuance_tokens': None,
            'burned_reissuance_tokens': 0
        },
        'contract': {
            'entity': {
            'domain': 'amole.org'
            },
            'issuer_pubkey': '03c5f0236f8f0b865d961ea22817621a3f645b39d1a38107255a74ec93b249f21b',
            'name': 'Ethiopian, Birr',
            'precision': 2,
            'ticker': 'ETB',
            'version': 0
        },
        'entity': {
            'domain': 'amole.org'
        },
        'precision': 2,
        'name': 'Ethiopian, Birr',
        'ticker': 'ETB'
    }
    """

.. autoclass:: bloxplorer.issued_assets.IssuedAssets
    :members:
