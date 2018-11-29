#!/usr/bin/python2.7

import requests

target_url = "http://192.168.44.101/dvwa/login.php"
data_dict = {"username":"admin","password":"password","Login":"submit"}
response = requests.post(target_url, data=data_dict)

print response
print response.content

