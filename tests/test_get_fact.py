# stdlib
import datetime
import re
import warnings
from functools import wraps
from typing import Callable

# 3rd party
import pytest
from apeye import RequestsURL
from domdf_python_tools.testing import check_file_regression
from pytest_regressions.file_regression import FileRegressionFixture

# this package
from rsc_on_this_day import clear_cache, date_arg_error_str, get_fact


def call_count(func: Callable) -> Callable:

	@wraps(func)
	def wrapper(*args, **kwargs):
		wrapper.call_count += 1  # type: ignore
		return func(*args, **kwargs)

	wrapper.call_count = 0  # type: ignore
	return wrapper


@pytest.fixture()
def monkeypatched_requests(monkeypatch):
	monkeypatch.setattr(RequestsURL, "get", call_count(RequestsURL.get))


@pytest.mark.parametrize(
		"date",
		[
				("January", 1),
				("February", 29),
				("July", 14),
				("October", 13),
				("December", 25),
				("January", '1'),
				("February", "29"),
				("July", "14"),
				("October", "13"),
				("December", "25"),
				(1, 1),
				(2, 29),
				(7, 14),
				(10, 13),
				(12, 25),
				('1', 1),
				('2', 29),
				('7', 14),
				("10", 13),
				("12", 25),
				(),
				]
		)
def test_get_fact(
		date,
		file_regression: FileRegressionFixture,
		monkeypatched_requests,
		monkeypatch,
		):
	with warnings.catch_warnings():
		warnings.filterwarnings("ignore", category=UserWarning)
		clear_cache()

	class MockedDate(datetime.date):

		@classmethod
		def today(cls):
			return datetime.date(2020, 12, 28)

	monkeypatch.setattr(datetime, "date", MockedDate)

	add = lambda args: '\n'.join(args)

	check_file_regression(add(get_fact(*date)), file_regression)

	# Subsequent runs to test cache

	check_file_regression(add(get_fact(*date)), file_regression)
	check_file_regression(add(get_fact(*date)), file_regression)

	assert RequestsURL.get.call_count == 1  # type: ignore


def test_get_fact_errors():
	with warnings.catch_warnings():
		warnings.filterwarnings("ignore", category=UserWarning)
		clear_cache()

	with pytest.raises(SyntaxError, match=re.escape(date_arg_error_str)):
		get_fact("January")
	with pytest.raises(SyntaxError, match=re.escape(date_arg_error_str)):
		get_fact(1)
	with pytest.raises(SyntaxError, match=re.escape(date_arg_error_str)):
		get_fact(day=3)

	with pytest.raises(ValueError, match=r"The given month \('Avril'\) is not recognised."):
		get_fact("Avril", 1)
	with pytest.raises(ValueError, match=r"The given month \(0\) is not recognised."):
		get_fact(0, 1)
	with pytest.raises(ValueError, match=r"The given month \(13\) is not recognised."):
		get_fact(13, 1)
	with pytest.raises(ValueError, match="Invalid day 0 for month 'January'"):
		get_fact(1, 0)
	with pytest.raises(ValueError, match="Invalid day 32 for month 'January'"):
		get_fact(1, 32)
	with pytest.raises(ValueError, match="Invalid day 30 for month 'February'"):
		get_fact(2, 30)
