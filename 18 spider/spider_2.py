#!/usr/bin/python

import requests
import re
import urlparse

target_url = "http://192.168.44.101"
target_links = []

def extract_links_from(url):
	response = requests.get(url)
	return re.findall('(?:href=")(.*?)"',response.content)

href_links = extract_links_from(target_url)

for link in href_links:
	link = urlparse.urljoin(target_url,link)

	if "#" in link:	# #r refers to original page so avoid duplicate page again and again
		link = link.split("#")[0]

	if target_url in link and link not in target_links: #to avoid repeating the same url
		target_links.append(link)
		print link

