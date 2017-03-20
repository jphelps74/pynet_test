#!/usr/bin/env python
f = open("ex2.txt", "w")
f.write("add this to the file\n")
f.close()
f = open("ex2.txt")
output = f.read()
print output
