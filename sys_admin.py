# Python3.6
# Coding: utf-8

import subprocess


command = "uname"
commandArgument = "-a"
print(f'Gathering system information with command: {command}{commandArgument}')
subprocess.run([command, commandArgument])

command = "ps"
commandArgument = "-x"
print(f'Gathering system process information with command: {command}{commandArgument}')
subprocess.run([command, commandArgument])