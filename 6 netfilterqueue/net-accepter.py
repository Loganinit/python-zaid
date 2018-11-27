#!/usr/bin/python2.7
#capture the request packet from client and save to a queue using iptables and alter send or recieve modified packet
#iptables commands iptables -I FORWARD -j NFQUEUE --queue-num 0

import netfilterqueue


def process_packet(packet):
	print packet
	packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0,process_packet)
queue.run()


