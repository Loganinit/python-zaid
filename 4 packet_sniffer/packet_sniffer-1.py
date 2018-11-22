#!/usr/bin/python2

import scapy.all as scapy

def sniff(interface):

	scapy.sniff(iface = interface, store = False, prn = process_sniffed_packet)
	#scapy.sniff to sniff the packet in specified interface and said not to keep in buffer by store=False 
	#pwn meaning is owned or compromised what sniff the packet what functions to do we give process_sniffed_packet which just print the packet
def process_sniffed_packet(packet):

	print packet
	print "-"*100


sniff('wlp3s0')