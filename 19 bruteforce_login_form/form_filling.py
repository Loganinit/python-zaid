#!/usr/bin/python2.7
#fill form with scipt by passing the value in data_dict then send that has POST Request
#we can automate the form filling process by import data from file and by put in loop to fill each and every data and exit after filing the final data
#the html_form.zip is given to test this script
#put the files in /var/www/html/* location
#start your own web server and test it !!

import requests

target_url = "http://127.0.0.1/process.php"
data_dict = {"user":"admin","pass":"password","Login":"submit"}
response = requests.post(target_url, data=data_dict)

print response
print response.content

