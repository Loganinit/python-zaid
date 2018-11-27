#!/usr/bin/python

import subprocess
import re

ifconf = subprocess.check_output(["ifconfig","enp2s0"])
print ifconf

mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconf)

print mac.group(0)