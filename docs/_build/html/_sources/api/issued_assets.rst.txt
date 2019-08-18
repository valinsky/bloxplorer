.. _issues_assets:

Issued Assets
=============

The Issued Assets class is available only for the Elements / Liquid explorer.

Usage
*****

.. code-block:: python

    from bloxplorer import liquid_explorer as explorer

    result = explorer.assets.get('issued_assets_hash')
    print(result.data)

.. autoclass:: bloxplorer.issued_assets.IssuedAssets
    :members:
