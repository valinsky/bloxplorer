Bloxplorer - Bitcoin and Liquid Blockchain Explorer
===================================================

|circle| |version| |license| |downloads|

:ref:`Quickstart <quickstart>`


**Bloxplorer** is a simple yet very effective Bitcoin and Liquid blockchain explorer.

It allows developers to make use of the full power of the `Blockstream Esplora HTTP API 
<https://github.com/Blockstream/esplora/blob/master/API.md>`_ through a clean Python interface.

.. code-block:: python

    from bloxplorer import bitcoin_explorer

    response = bitcoin_explorer.blocks.get_last_height()
    print(response.data)
    '586438'


.. |circle| image:: https://circleci.com/gh/valinsky/bloxplorer/tree/master.svg?style=shield
    :target: https://circleci.com/gh/valinsky/bloxplorer/tree/master

.. |version| image:: https://img.shields.io/badge/version-0.1.3-blue
    :target: https://pypi.org/project/bloxplorer/

.. |license| image:: https://img.shields.io/badge/license-MIT-orange
    :target: https://github.com/valinsky/bloxplorer/blob/master/LICENSE

.. |downloads| image:: https://pepy.tech/badge/bloxplorer
    :target: https://pepy.tech/project/bloxplorer/

.. toctree::
    :maxdepth: 2
    :numbered:
    :glob:

    quickstart
    api
