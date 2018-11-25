#!/usr/bin/python
'''
Storing the interface and mac addr to a variable and 
then pass the value to the command directly
'''

import subprocess

interface = "enp2s0"
macaddr = "00:11:22:33:44:55"

print "[+] Changing Mac Address of Interface %s to %s"%(interface,macaddr)


subprocess.call("ifconfig %s down"%interface,shell=True)
subprocess.call("ifconfig %s hw ether %s"%(interface,macaddr),shell=True)
subprocess.call("ifconfig %s up"%interface,shell=True)