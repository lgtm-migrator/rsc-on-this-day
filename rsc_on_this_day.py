import requests
from bs4 import BeautifulSoup
#from datetime import datetime as dt
import datetime
import requests_cache
from cashier import cache


# Initialise requests-cache
expire_after = datetime.timedelta(hours=5)
requests_cache.install_cache(expire_after=expire_after)
requests_cache.remove_expired_responses()

# -----------------------------------------

# TODO: custom dates

@cache(cache_file="cache.db", cache_time=18000, retry_if_blank=True)
def query_website():
	page = requests.get("http://www.rsc.org/learn-chemistry/collections/chemistry-calendar")
	
	soup = BeautifulSoup(page.content, "html.parser")
	
	# print(datetime.datetime.today().strftime('%d %B'))
	
	header = soup.find("div", {"class": "description"}).previousSibling.previousSibling.get_text().strip()
	body = soup.find("div", {"class": "description"}).get_text().strip()
	
	return header, body

def main():
	header, body = query_website()
	print(header)
	print(body)

	
if __name__ == "__main__":
	main()

# TODO: Timeout