#!/usr/bin/env python

import commands

mount_str = commands.getoutput("df -k")

mount_list = mount_str.split("\n")

for line in mount_list[1:]:
  file_split = line.replace("%", "").split()
  if int(file_split[4]) > 95:
    print("this filesystem %s is greater than 95" % file_split[0])
