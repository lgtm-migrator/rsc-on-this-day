================================
RSC On This Day in Chemistry
================================

.. start short_desc

**Displays Royal Society of Chemistry "On This Day" facts.**

.. end short_desc

Displays Royal Society of Chemistry "On This Day" facts in your terminal.

.. start shields

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Docs
	  - |docs| |docs_check|
	* - Tests
	  - |travis| |actions_windows| |actions_macos| |coveralls| |codefactor|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Activity
	  - |commits-latest| |commits-since| |maintained|
	* - Other
	  - |license| |language| |requires| |pre_commit|

.. |docs| image:: https://img.shields.io/readthedocs/rsc_on_this_day/latest?logo=read-the-docs
	:target: https://rsc_on_this_day.readthedocs.io/en/latest/?badge=latest
	:alt: Documentation Status

.. |docs_check| image:: https://github.com/domdfcoding/rsc_on_this_day/workflows/Docs%20Check/badge.svg
	:target: https://github.com/domdfcoding/rsc_on_this_day/actions?query=workflow%3A%22Docs+Check%22
	:alt: Docs Check Status

.. |travis| image:: https://img.shields.io/travis/com/domdfcoding/rsc_on_this_day/master?logo=travis
	:target: https://travis-ci.com/domdfcoding/rsc_on_this_day
	:alt: Travis Build Status

.. |actions_windows| image:: https://github.com/domdfcoding/rsc_on_this_day/workflows/Windows%20Tests/badge.svg
	:target: https://github.com/domdfcoding/rsc_on_this_day/actions?query=workflow%3A%22Windows+Tests%22
	:alt: Windows Tests Status

.. |actions_macos| image:: https://github.com/domdfcoding/rsc_on_this_day/workflows/macOS%20Tests/badge.svg
	:target: https://github.com/domdfcoding/rsc_on_this_day/actions?query=workflow%3A%22macOS+Tests%22
	:alt: macOS Tests Status

.. |requires| image:: https://requires.io/github/domdfcoding/rsc_on_this_day/requirements.svg?branch=master
	:target: https://requires.io/github/domdfcoding/rsc_on_this_day/requirements/?branch=master
	:alt: Requirements Status

.. |coveralls| image:: https://img.shields.io/coveralls/github/domdfcoding/rsc_on_this_day/master?logo=coveralls
	:target: https://coveralls.io/github/domdfcoding/rsc_on_this_day?branch=master
	:alt: Coverage

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/domdfcoding/rsc_on_this_day?logo=codefactor
	:target: https://www.codefactor.io/repository/github/domdfcoding/rsc_on_this_day
	:alt: CodeFactor Grade

.. |pypi-version| image:: https://img.shields.io/pypi/v/rsc_on_this_day
	:target: https://pypi.org/project/rsc_on_this_day/
	:alt: PyPI - Package Version

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/rsc_on_this_day?logo=python&logoColor=white
	:target: https://pypi.org/project/rsc_on_this_day/
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/rsc_on_this_day
	:target: https://pypi.org/project/rsc_on_this_day/
	:alt: PyPI - Supported Implementations

.. |wheel| image:: https://img.shields.io/pypi/wheel/rsc_on_this_day
	:target: https://pypi.org/project/rsc_on_this_day/
	:alt: PyPI - Wheel

.. |license| image:: https://img.shields.io/github/license/domdfcoding/rsc_on_this_day
	:target: https://github.com/domdfcoding/rsc_on_this_day/blob/master/LICENSE
	:alt: License

.. |language| image:: https://img.shields.io/github/languages/top/domdfcoding/rsc_on_this_day
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/domdfcoding/rsc_on_this_day/v0.2.3
	:target: https://github.com/domdfcoding/rsc_on_this_day/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/domdfcoding/rsc_on_this_day
	:target: https://github.com/domdfcoding/rsc_on_this_day/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2020
	:alt: Maintenance

.. |pre_commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
	:target: https://github.com/pre-commit/pre-commit
	:alt: pre-commit

.. end shields


Installation
-------------

.. start installation

``rsc_on_this_day`` can be installed from PyPI.

To install with ``pip``:

.. code-block:: bash

	$ python -m pip install rsc_on_this_day

.. end installation

Once installed, ``rsc_on_this_day`` can be run by typing:

.. parsed-literal::

        $ rsc_on_this_day

If ``rsc_on_this_day`` is not installed in a directory in ``$PATH``, you may need to add ``~/.local/bin/`` to your ``$PATH``.



Adding to ``~/.bashrc``
-----------------------

``rsc_on_this_day`` can be run every time you open a terminal by adding ``rsc_on_this_day`` to your ``~/.bashrc`` file. For example:

.. parsed-literal::

    $ echo "rsc_on_this_day" >> ~/.bashrc
