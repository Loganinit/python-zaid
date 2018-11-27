#!/usr/bin/python2.7
#capture the request packet from client and save to a queue using iptables and alter to send or recieve modified packet
#drop the packet cut the netconnection because packet.accept() is not specified

import netfilterqueue


def process_packet(packet):
	print packet

queue = netfilterqueue.NetfilterQueue()
queue.bind(0,process_packet)
queue.run()


