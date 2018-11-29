#!/usr/bin/python2
#put the script in startup folder to run when the system boots
#put in /etc/init.d/script.py make executable sudo chmod 755 /etc/init.d/scipt.py
#Register script to be run at startup sudo update-rc.d superscript defaults

import scapy.all as scapy

def getmac(ip):

	arp_request_header = scapy.ARP(pdst = ip)
	ether_header = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_request_packet = ether_header/arp_request_header
	answered_list = scapy.srp(arp_request_packet,timeout=1,verbose=False)[0]
	return  answered_list[0][1].hwsrc

def sniff(interface):

	scapy.sniff(iface=interface,store=False,prn=process_sniffed_packet)

def process_sniffed_packet(packet):

	if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op==2:
		try:
			real_mac = getmac(packet[scapy.ARP].psrc)
			response_mac = packet[scapy.ARP].hwsrc

			if real_mac != response_mac:
				print ("[+] You are under attack !!")

		except IndexError:
			pass
			
sniff("wlan0")
