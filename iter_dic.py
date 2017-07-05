#!/usr/bin/env python

import commands
new_array = []

file_passwd = commands.getoutput("cat /etc/passwd")

passwd_array = file_passwd.split("\n")

for line in passwd_array:
  if line.startswith("#"):
	continue
  

  spilt_field = line.split(":")
  new_array.append([spilt_field[0], spilt_field[2:]])


print(new_array)
