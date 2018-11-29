#!/usr/bin/python

import requests
from BeautifulSoup import BeautifulSoup

def request(url):
	try:
		return requests.get(url)
	except requests.exceptions.ConnectionError:
		pass

target_url = "http://192.168.44.101/mutillidae/index.php?page=dns-lookup.php"
response = request(target_url)

parsed_html = BeautifulSoup(response.content)
forms_list = parsed_html.findAll("form")

for form in forms_list:
	print "Action: ",form.get("action")
	print "Method: ",form.get("method")
	print "EncType: ",form.get("enctype")
	print "ID: ",form.get("id")


	inputs_list = form.findAll("input")

	for input in inputs_list:
		input_name = input.get("name")
		print "Name: ",input_name
 	