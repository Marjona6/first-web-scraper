# import statements
import urllib2
# urllib2.urlopen("http://www.python.org/")
import csv
import requests
from BeautifulSoup import BeautifulSoup

#
url = "https://stackoverflow.com/jobs/132900/front-end-developer-bookingcom?sec=False"
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

# Generic job info
job_info = soup.find("div", id="job-detail")
about_job_items_keys = job_info.findAll("span", attrs = {"class": "-key"})
about_job_items_values = job_info.findAll("span", attrs = {"class": "-value"})

# Position location
location = soup.find("div", attrs = {"class": "-location"}).text.strip()
# print location

# print about_job_items_keys
# print about_job_items_values

# for datum in soup.find_all("div", id="job-detail"):
# 	item_key = datum.find("span", attrs = {"class": "-key"})
# 	item_value = datum.find("span", attrs = {"class": "-value"})
# 	print "{} is the key for the value {}".format(item_key, item_value)