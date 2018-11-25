#!/usr/bin/python

import requests
import re
import urlparse

target_url = "http://192.168.44.101"
target_links = []

def extract_links_from(url):
	response = requests.get(url)
	return re.findall('(?:href=")(.*?)"',response.content)

def crawl(url):
	href_links = extract_links_from(url)

	for link in href_links:
		link = urlparse.urljoin(url,link)

		if "#" in link:	# #r refers to original page so avoid duplicate page again and again
			link = link.split("#")[0]

		if target_url in link and link not in target_links: #to avoid repeating the same url
			target_links.append(link)
			print link
			crawl(link) #recurrsively crawling

crawl(target_url)