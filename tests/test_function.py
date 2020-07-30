"""
Rudimentary test to ensure everything works without error.
"""

import requests_cache  # type: ignore
from rsc_on_this_day import main, cache_dir


def test_function():
	requests_cache.install_cache(str(cache_dir / "requests_cache"), expire_after=2500000)
	requests_cache.remove_expired_responses()

	main([])  # Current day
	main(["1", "2"])  # 2nd Jan
