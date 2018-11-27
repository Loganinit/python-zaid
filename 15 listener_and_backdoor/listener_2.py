#!/usr/bin/python

import socket


class Listener:

	def __init__(self,ip,port):
		listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		#options to reuse sockets
		#listener.bind(("localhost",1234))
		listener.bind((ip,port))
		listener.listen(0)
		print "[+] Waiting for Incoming Connection"
		#listen for connecion backlog is set to 0 don't need to wory about 0
		self.connection,address = listener.accept()
		print "[+] Got a Connection from " + str(address)


	def execute_remotely(self,command):
		self.connection.send(command)
		return self.connection.recv(1024)

	def run(self):
		while True:
			command = raw_input(">> ")
			result = self.execute_remotely(command)
			print result

my_listener = Listener("localhost",1234)
my_listener.run()