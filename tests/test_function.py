"""
Rudimentary test to ensure everything works without error.
"""

# 3rd party
import requests_cache  # type: ignore

# this package
from rsc_on_this_day import cache_dir, main


def test_function():
	requests_cache.install_cache(str(cache_dir / "requests_cache"), expire_after=2500000)
	requests_cache.remove_expired_responses()

	main([])  # Current day
	main(['1', '2'])  # 2nd Jan
