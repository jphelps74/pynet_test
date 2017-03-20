#!/usr/bin/env python
ip_addr = raw_input('IP Address: ')
ip_addr.split(".")
print "{:12}{:12}{:12}{:12}".format(ip_addr.split(".")[0],ip_addr.split(".")[1],ip_addr.split(".")[2],ip_addr.split(".")[3])

