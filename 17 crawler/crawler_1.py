#!/usr/bin/python

#discover sub domain
import requests

def request(url):
	try:
		return requests.get("http://" + url)
	except requests.exceptions.ConnectionError:
		pass

target_url = "google.com"

with open("subdomain.list","r") as wordlist_file:
	for line in wordlist_file:
		word = line.strip()
		test_url = word + "." + target_url
		response = request(test_url)
		if response :
			print "[+] Discovered subdomain ----> "+test_url
		