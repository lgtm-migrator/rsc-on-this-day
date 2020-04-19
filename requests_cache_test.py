import os

import requests
import requests_cache

# Make sure there is no cache already
if os.path.isfile("/tmp/requests_cache_test.sqlite"):
	os.unlink("/tmp/requests_cache_test.sqlite")

target_url = "http://wikipedia.org"


def perform_request():
	"""Function to perform the request"""
	r = requests.get(target_url, stream=True)
	print(type(r.raw))
	with r.raw:
		pass


print("\nRequest without cache")
perform_request()

# Again with cache
print("\nRequest with cache, 1st time")
requests_cache.install_cache("/tmp/requests_cache_test")
perform_request()

# Query a second time now it's cached
print("\nRequest with cache, 2nd time")
perform_request()
