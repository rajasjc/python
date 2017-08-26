#!/usr/bin/env python
import commands

pass_string = commands.getoutput('cat /etc/passwd')

pass_list = pass_string.split('\n')

data = dict()
value = []
value_1 = []
for line in pass_list:
 if line.startswith('#'):
  continue
 line_list = line.split(':')
 value_1 = [ line_list[2], line_list[3], line_list[-1] ]
 data[line_list[0]] = value_1

print(data)
 
