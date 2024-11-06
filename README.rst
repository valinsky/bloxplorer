*************************
🔥🔥🔥 Bloxplorer 🔥🔥🔥 
*************************

======================================
Bitcoin and Liquid Blockchain Explorer
======================================

|CI| |version| |license| |downloads|

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
    '869056'

Full documentation is available `here <https://valinsky.github.io/bloxplorer/>`_.

Installation
------------

To install the Bloxplorer package just run this command in your favorite terminal:

>>> pip install bloxplorer

Links
-----

* `Documentation <https://valinsky.github.io/bloxplorer/>`_
* `GitHub <https://github.com/valinsky/bloxplorer>`_
* `Pypi <https://pypi.org/project/bloxplorer>`_
* `CI <https://github.com/valinsky/bloxplorer/actions/>`_
* `License <https://github.com/valinsky/bloxplorer/blob/master/LICENSE>`_


.. |CI| image:: https://github.com/valinsky/bloxplorer/actions/workflows/main.yml/badge.svg
    :target: https://github.com/valinsky/bloxplorer/actions/

.. |version| image:: https://img.shields.io/badge/version-0.1.10-blue
    :target: https://pypi.org/project/bloxplorer/

.. |license| image:: https://img.shields.io/badge/license-MIT-orange
    :target:  https://github.com/valinsky/bloxplorer/blob/master/LICENSE

.. |downloads| image:: https://pepy.tech/badge/bloxplorer
    :target: https://pepy.tech/project/bloxplorer/
