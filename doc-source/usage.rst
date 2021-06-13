=========
Usage
=========

rsc-on-this-day
--------------------

.. click:: rsc_on_this_day.__main__:main
	:prog: rsc-on-this-day
	:nested: none


.. latex:vspace:: 20px

Examples
---------

.. prompt:: bash

	rsc_on_this_day

* Display the "On This Day In Chemistry" fact for today.

.. prompt:: bash

	rsc_on_this_day Apr 1

* Display the "On This Day In Chemistry" fact for April 1st.

.. prompt:: bash

	rsc_on_this_day 12 25

* Display the "On This Day In Chemistry" fact for 25 December.

.. prompt:: bash

	rsc_on_this_day --clear-cache

* Clear any cached data.

.. prompt:: bash

	rsc_on_this_day October 13 --width 80

* Display the "On This Day In Chemistry" fact for October 13th, with at most 80 characters per line.


Adding to ``~/.bashrc``
-----------------------

``rsc-on-this-day`` can be run every time you open a terminal by adding ``rsc-on-this-day`` to your ``~/.bashrc`` file.
For example:

.. prompt:: bash

	echo "rsc-on-this-day" >> ~/.bashrc
