#!/usr/bin/env python
import re
f = open("show_int_fa4.txt")
output = f.read()
for line in output.split("/n"):
    bytesin = re.search(r'(.*)\ packets input, (.*) bytes', line)
#18047726 packets output, 2073955919 bytes, 0 underruns
    bytesout = re.search(r'(.*)\ packets output, (.*) bytes,', line)
    print "{} {}".format(bytesin.group(1), bytesin.group(2))
    print "{} {}".format(bytesout.group(1), bytesout.group(2)) 
