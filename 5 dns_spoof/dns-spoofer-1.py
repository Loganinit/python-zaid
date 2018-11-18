#!/usr/bin/python2
#capture the request packet from client and save to a queue using iptables and alter send or recieve modified packet
#convert the raw packet to scapy packet to modify the request
#pip install NetfilterQueue
#apt-get install build-essential python-dev libnetfilter-queue-dev

import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
	scapy_packet = scapy.IP(packet.get_payload())
	#convert raw packet unreadable one into scapy packet

	if scapy_packet.haslayer(scapy.DNSRR):		#if packet has DNS Resource Record from response packet it's only in response packet
		print scapy_packet.show()

	packet.accept()		#accept the packet to process else it is remains in queue forever

queue = netfilterqueue.NetfilterQueue()
#create a netfilterqueue instance
queue.bind(0,process_packet)
#blind the queue number 0 where we create a queue zero in iptables
queue.run()
#run the queue else it will not run

