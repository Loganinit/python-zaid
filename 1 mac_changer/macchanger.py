#!/usr/bin/python2.7

import subprocess
import optparse
import re

def macchanger(interface,macaddr):

	subprocess.call(["ifconfig",interface,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",macaddr])
	subprocess.call(["ifconfig",interface,"up"])

	print "[+] Changing Mac Address of Interface %s to %s"%(interface,macaddr)

def get_argument():

	parser=optparse.OptionParser()	
	parser.add_option("-i","--interface",dest="interface",help="Interface to change the mac address")
	parser.add_option("-m","--mac",dest="new_mac",help="add new mac address")
	(options,arguments) = parser.parse_args()

	if not options.interface:
		parser.error("[-] Specify an Interface use python macchanger --help for more details")
	elif not options.new_mac:
		parser.error("[-] Specify an MacAddr use python macchanger --help for more details")

	return options

def getmac(interface):

	ifconfig_result = subprocess.check_output(["ifconfig",interface])
	current_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)

	if current_mac:
		return current_mac.group(0)
	else:
		return None

options= get_argument()		
#option gets the value of interface and mac returned by get_argument function

macchanger(options.interface,options.new_mac)
#main program which change the mac address

final_mac = getmac(options.interface)
#verify whether the mac is changed or Not

if final_mac == options.new_mac :
	print "Mac Address Successfully Chaged with new one %r"%final_mac
else:
	print "Error Occured Fix It"