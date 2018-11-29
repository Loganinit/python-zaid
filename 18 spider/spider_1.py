#!/usr/bin/python

import requests
import re

target_url = "http://192.168.44.101"

def extract_links_from(url):
	response = requests.get(url)
	return re.findall('(?:href=")(.*?)"',response.content)

href_links = extract_links_from(target_url)

for link in href_links:
	print link

