#!/usr/bin/python2

import argparse
import subprocess
import re

def get_argument():

	parser=argparse.ArgumentParser()	
	parser.add_argument("-i","--interface",dest="interface",help="Specify Interface to change the MAC")
	parser.add_argument("-m","--macaddr",dest="macaddr",help="Specify MAC address to change")
	options = parser.parse_args()

	if not options.interface:
		parser.error("[-] Specify an Interface use python macchanger --help for more details")
	elif not options.macaddr:
		parser.error("[-] Specify an MacAddr use python macchanger --help for more details")

	return options

def macchanger(interface,macaddr):

	subprocess.call(["ifconfig",interface,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",macaddr])
	subprocess.call(["ifconfig",interface,"up"])

	print "[+] Changing Mac Address of Interface %s to %s"%(interface,macaddr)

def getmac(interface):

	ifconfig_result = subprocess.check_output(["ifconfig",interface])
	current_mac = re.findall(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)

	if current_mac:
		return current_mac[0]
	else:
		return None


options = get_argument()

macchanger(options.interface,options.macaddr)

final_mac = getmac(options.interface)

if final_mac == options.macaddr:
	print "Mac Address Successfully Chaged with new one %r"%final_mac
else:
	print "Error Occured Fix It"