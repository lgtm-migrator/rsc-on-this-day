****************
rsc_on_this_day
****************

Displays Royal Society of Chemistry "On This Day" facts in your terminal.

Synopsis
-----------

rsc_on_this_day [*OPTION*]... [*month*] [*day*]


Description
-------------

Displays Royal Society of Chemistry "On This Day In Chemistry" facts in your
terminal.

**positional arguments:**

	**month**
		The name or number of the month of the fact to display.

	**day**
		The day number of the fact to display.

**optional arguments:**

	**-h**, **--help**
		Show usage information and exit.

	**-w**, **--width**\=\*WIDTH*
		The number of characters per line of the output.
		Default 80. Set to -1 to disable wrapping.

	**--clear-cache**
		Clear any cached data and exit.

	**--version**
		Show the version number and exit.

If requesting a specific date both the month and day must be given.


Examples
---------

rsc_on_this_day
	Display the "On This Day In Chemistry" fact for today.

rsc_on_this_day Apr 1
	Display the "On This Day In Chemistry" fact for April 1st.

rsc_on_this_day 12 25
	Display the "On This Day In Chemistry" fact for 25 December.

rsc_on_this_day --clear-cache
	Clear any cached data.

rsc_on_this_day October 13 --width 80
	Display the "On This Day In Chemistry" fact for October 13th, with at most 80 characters per line.


Installation
-------------

``rsc_on_this_day`` can be installed with pip:


.. parsed-literal::

	$ pip install rsc_on_this_day


Once installed, ``rsc_on_this_day`` can be run by typing:

.. parsed-literal::

	$ rsc_on_this_day

If ``rsc_on_this_day`` is not installed in a directory in ``$PATH``, you may need to add ``~/.local/bin/`` to your ``$PATH``.

Adding to ``~/.bashrc``
-----------------------

``rsc_on_this_day`` can be run every time you open a terminal by adding ``rsc_on_this_day`` to your ``~/.bashrc`` file. For example:

.. parsed-literal::

	$ echo "rsc_on_this_day" >> ~/.bashrc

Reporting Bugs
---------------

Please use the GitHub issue tracker to report bugs: <`https://github.com/domdfcoding/rsc-on-this-day/issues <https://github.com/domdfcoding/rsc-on-this-day/issues>`_>

See Also
-----------
fortune(6)
