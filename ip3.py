#!/usr/bin/env python
ip_addr = raw_input('IP Address: ')
ip_addr = ip_addr.split(".")
#print "{:12}{:12}{:12}{:12}".format(*ip_addr)
ip_list = ip_addr
#print ip_list
ip_list[3] = 0
#print ip_list
a = int(ip_list[0])
b = int(ip_list[1])
c = int(ip_list[2])
d = int(ip_list[3])
print "{} {} {} {}".format(bin(a), bin(b), bin(c), bin(d))
print "{:12}{:12}{:12}{:12}".format(*ip_addr)

