#!/usr/bin/python2

import requests

def download(url):

	get_request = requests.get(url)
	#print (get_request.content)
	#print (get_request)

	with open("lamborghini.jpeg","w") as file:
		file.write(get_request.content)

download("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcQC7LyJgwpvRiGdxviJlf1O64vr8QUgB7ktqe3MYCapQIltZRig")

