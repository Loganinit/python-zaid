#!/usr/bin/python2

import scapy.all as scapy
import argparse

def get_ip_range():

	parser=argparse.ArgumentParser()	
	parser.add_argument("-r","--range",dest="ipadrr",help="Specify an IP Address or a range of IP Address")
	options = parser.parse_args()

	if not options.ipadrr:
		parser.error("[-] Specify an IP Address or a range of IP Address --help for more details")

	return options

def scan(ip):
	
	arp_request_header = scapy.ARP(pdst = ip)
	ether_header = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_request_packet = ether_header/arp_request_header
	answered_list = scapy.srp(arp_request_packet,timeout=1,verbose=False)[0]

	clients_list = []
	for elements in answered_list:
		client_dict = {"ip":elements[1].psrc,"mac":elements[1].hwsrc}
		clients_list.append(client_dict)
	
	return clients_list

def print_result(result_list):

	print "\nIpAdrr\t\t\tMacAddr"
	print "------------------------------------------"
	for client in result_list:
		print client['ip'],"\t\t",client['mac']

ip = get_ip_range()

scan_result = scan(ip.ipadrr)

print_result(scan_result)

print "------------------------------------------"
