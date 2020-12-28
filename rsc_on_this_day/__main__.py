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
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
#  OR OTHER DEALINGS IN THE SOFTWARE.
#

# stdlib
import sys
import textwrap
from typing import Union

# 3rd party
import click
from click import Context, Parameter, version_option
from consolekit import click_command
from domdf_python_tools.dates import check_date, parse_month

# this package
import rsc_on_this_day
from rsc_on_this_day import __version__

__all__ = ["main"]


def clear_cache_callback(context: Context, param: Parameter, value):
	if value:
		sys.exit(rsc_on_this_day.clear_cache())


@click.argument(
		"month",
		type=click.INT,
		default=None,
		required=False,
		)
@click.argument(
		"day",
		type=click.INT,
		default=None,
		required=False,
		)
@click.option(
		"-w",
		"--width",
		type=click.INT,
		default=80,
		help="The number of characters per line of the output. Default 80. Set to -1 to disable wrapping."
		)
@click.option(
		"--clear-cache",
		is_flag=True,
		default=False,
		help="Clear any cached data and exit.",
		callback=clear_cache_callback,
		)
@version_option(__version__)
@click_command()
def main(
		month: Union[str, int, None] = None,
		day: Union[str, int, None] = None,
		width: int = 80,
		clear_cache: bool = False,
		):
	"""
	Display the Royal Society of Chemistry "On This Day In Chemistry" fact for the given day.

	If no date is given the current date is used.
	"""

	if clear_cache:
		sys.exit(rsc_on_this_day.clear_cache())

	if (month and day is None) or (day and month is None):
		raise click.UsageError(rsc_on_this_day.date_arg_error_str)

	if month is not None and day is not None:
		try:
			month = parse_month(month)
		except ValueError:
			raise click.UsageError(f"Invalid value for month: {month}")

		# Check that the date is valid
		if not check_date(month, day):  # type: ignore
			click.UsageError(f"{day}/{month} is not a valid date.")

	header, body = rsc_on_this_day.get_fact(month, day)

	if width > 0:
		header = textwrap.fill(header, width)
		body = textwrap.fill(body, width)

	# print(f"{day}/{month}")
	print(header)
	print(body)


if __name__ == "__main__":
	sys.exit(main())
