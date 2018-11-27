#!/usr/bin/python

import scapy.all as scapy

def scan(ip):
	scapy.arping(ip)
	#Well defined method to do the arp resquest respond work with a single line


scan("192.168.43.1/24")