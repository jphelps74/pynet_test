#!/usr/bin/env python
my_list = ['Uber', 10, 22.0, 'SF', 15]
print my_list
new_list = my_list[:]
new_list.extend([12, 'test123'])
print new_list
new_list.pop(0)
print new_list
new_list.sort()
print new_list 
