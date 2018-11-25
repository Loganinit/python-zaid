#!/usr/bin/python

import scapy.all as scapy
import optparse


def get_ip():

	parser=optparse.OptionParser()	
	parser.add_option("-t","--target",dest="ipadrr",help="Specify an IP Address or a range of IP Address")
	(options,argument) = parser.parse_args()
	#(values,options) = ("192.168.43.1",-ip)

	if not options.ipadrr:
		parser.error("[-] Specify an IP Address or a range of IP Address --help for more details")

	return options

def scan(ip):
	
	arp_request = scapy.ARP(pdst = ip)
	#creating arp_request object with dst_ip=user_input_ip

	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	#create a broadcast object to have Ether frame property with dst_mac = ff:ff:ff:ff:ff:ff

	arp_request_broadcast = broadcast/arp_request
	#combine the Ether frame to arp_request to send

	answered_list = scapy.srp(arp_request_broadcast,timeout=1)[0]
	#scapy.srp to send the packet in layer2 Ether fram which returns 2 value answered,unanswered
	#timeout=1 specify wait for 1 sec not till you getting replay	

	clients_list = []
	#declaring a list to store a dict values of ip and mac in it
	#nice way of storing a data and use for later use

	for elements in answered_list:
		client_dict = {"ip":elements[1].psrc,"mac":elements[1].hwsrc}
		#declare a dict to get ip and mac
		clients_list.append(client_dict)
	
	return clients_list


def print_result(result_list):

	print "IpAdrr\t\t\tMacAddr"
	print "------------------------------------------"
	for client in result_list:
		print client['ip'],"\t\t",client['mac']

ip = get_ip()
#get the ip range to ip variable

scan_result = scan(ip.ipadrr)
#use the ipaddr instance to use input ip to scan function

print_result(scan_result)
#represent the scan result in another function name print_result
