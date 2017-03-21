#!/usr/bin/env python
f = open("show_ip_bgp.txt")
output = f.read()
for line in output.split("\n"):
    if " *   " in line:
        ip = line.split()[1]
        asn = line.split()[5:-1]
        as_path  = " ".join(asn)
        print "{} {}".format(ip, as_path)

