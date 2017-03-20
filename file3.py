#!/usr/bin/env python
f = open("ex2.txt", "a")
new_string = raw_input('Enter String: ')
new_string = new_string + '\n'
f.write(new_string)
f.close()
f = open("ex2.txt")
output = f.read()
print output
