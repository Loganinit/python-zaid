#!/usr/bin/python
'''
Getting the value for  the interface and mac addr to a variable and 
then pass the value to the command directly
'''

import subprocess

interface = raw_input("Interface> ")
macaddr = raw_input("MacAddr> ")

print "[+] Changing Mac Address of Interface %s to %s"%(interface,macaddr)


subprocess.call("ifconfig %s down"%interface,shell=True)
subprocess.call("ifconfig %s hw ether %s"%(interface,macaddr),shell=True)
subprocess.call("ifconfig %s up"%interface,shell=True)