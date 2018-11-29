#!/usr/bin/python2.7
#dicover subdomains of domain by bruteforcing common sub domains to the domain and
#if we get a respond then the sub-domain exist 

import requests
from datetime import datetime

start=datetime.now()

def request(url):
	try:
		return requests.get("http://" + url)
	except requests.exceptions.ConnectionError:
		pass

target_url = "google.com"
#subdomain_list = []
file = open("googlesubdomain.txt","aw")
with open("top_10_subdomain.txt","r") as wordlist_file:
	for line in wordlist_file:
		word = line.strip()
		test_url = word + "." + target_url
		response = request(test_url)
		if response :
			print "[+] Discovered subdomain ----> "+test_url
			#subdomain_list.append(test_url)
			file.write(test_url+"\n")
file.close()

stop=datetime.now()

totaltime=stop-start
print "\n[***]TotalTimeTaken = ",totaltime