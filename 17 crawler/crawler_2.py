#!/usr/bin/python

#discover hidden directory

import requests

def request(url):
	try:
		return requests.get("http://" + url)
	except requests.exceptions.ConnectionError:
		pass

target_url = "192.168.44.101/mutillidae"

with open("common.txt","r") as wordlist_file:
	for line in wordlist_file:
		word = line.strip()
		test_url = target_url + "/" + word
		response = request(test_url)
		if response :
			print "[+] Discovered URL ----> " + test_url
		