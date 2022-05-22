#! /usr/bin/env python3

import getpass
import sys
import telnetlib

HOST = "192.168.100.10"
user = raw_input("Enter your tenet username:")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user = "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")


tn.write("int l0\n")
tn.write("ip add 1.1.1.1 255.255.255.255")
tn.write("")
tn.write("enable\n")
tn.write("cisco\n")
