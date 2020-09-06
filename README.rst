*************************
🔥🔥🔥 Bloxplorer 🔥🔥🔥 
*************************

======================================
Bitcoin and Liquid Blockchain Explorer
======================================

|circle| |version| |license| |downloads|

**Bloxplorer** is a simple yet very effective Bitcoin and Liquid blockchain explorer.

It allows developers to make use of the full power of the `Blockstream Esplora HTTP API 
<https://github.com/Blockstream/esplora/blob/master/API.md>`_ through a clean Python interface.

Usage
-----

Using the Bloxplorer package is easy and straightforward, as it should be.

.. code-block:: python

    from bloxplorer import bitcoin_explorer

    response = bitcoin_explorer.blocks.get_last_height()
    print(response.data)
    '586438'

Full documentation is available at https://valinsky.github.io/bloxplorer/

Installation
------------

To install the Bloxplorer package just run this command in your favorite terminal:

>>> pip install bloxplorer

Links
-----

* Documentation: https://valinsky.github.io/bloxplorer/
* GitHub: https://github.com/valinsky/bloxplorer
* Pypi: https://pypi.org/project/bloxplorer
* CircleCI: https://circleci.com/gh/valinsky/bloxplorer/tree/master
* License: https://github.com/valinsky/bloxplorer/blob/master/LICENSE

Tip me `+gentleviolet421 <https://paynym.is/+gentleviolet421>`_

For more on paynyms `check this out. <https://paynym.is>`_

.. |circle| image:: https://circleci.com/gh/valinsky/bloxplorer/tree/master.svg?style=shield
    :target: https://circleci.com/gh/valinsky/bloxplorer/tree/master

.. |version| image:: https://img.shields.io/badge/version-0.1.8-blue
    :target: https://pypi.org/project/bloxplorer/

.. |license| image:: https://img.shields.io/badge/license-MIT-orange
    :target:  https://github.com/valinsky/bloxplorer/blob/master/LICENSE

.. |downloads| image:: https://pepy.tech/badge/bloxplorer
    :target: https://pepy.tech/project/bloxplorer/
