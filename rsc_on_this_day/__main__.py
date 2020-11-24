#!/usr/bin/env python3
#
#  rsc_on_this_day.py
"""
Displays Royal Society of Chemistry "On This Day In Chemistry" facts in your terminal.
"""
#
#  Copyright © 2019-2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  Cached copies of the RSC On This Day website Copyright © 2020 Royal Society of Chemistry
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

# stdlib
import sys

# 3rd party
import requests_cache  # type: ignore

# this package
from rsc_on_this_day import cache_dir, main

if __name__ == "__main__":  # pragma: no cover
	# Set up requests_cache and keep cache for about a month
	# We do this here so we don't interfere with programs that import from this program
	requests_cache.install_cache(str(cache_dir / "requests_cache"), expire_after=2500000)
	requests_cache.remove_expired_responses()

	main(sys.argv[1:])
