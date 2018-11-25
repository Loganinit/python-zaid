#!/usr/bin/python

import subprocess

subprocess.call("ifconfig enp2s0 down",shell=True)
subprocess.call("ifconfig enp2s0 hw ether 00:11:22:33:44:55",shell=True)
subprocess.call("ifconfig enp2s0 up",shell=True)