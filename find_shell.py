#!/usr/bin/env python

import commands

passwd_file = commands.getoutput('cat /etc/passwd')
data = {}
def find_shel(uid):
 for line in passwd_file.split('\n'):
  if line.startswith('#'):
   continue
  line_s = line.split(':')
  if line_s[2] == uid:
   data[line_s[0]] = line_s[-1]
 return(data)

print_this = find_shel('231')
print(print_this)
