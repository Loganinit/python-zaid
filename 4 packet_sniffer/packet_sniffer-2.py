#!/usr/bin/python2
#filtering with 3 rd party module scapy_http for request method 
#pip install scapy_http

import scapy.all as scapy
from scapy.layers import http

def sniff(interface):

	scapy.sniff(iface = interface, store = False, prn = process_sniffed_packet,filter = "port 80")
	#only port 80 that is http traffic will be sniffed and https also which is http+ssl traffic

def process_sniffed_packet(packet):

	if packet.haslayer(http.HTTPRequest):
		print packet.show()


sniff('wlp3s0')