#!/usr/bin/env python

import commands

passwd_str = commands.getoutput("cat /etc/passwd")

passwd_list = passwd_str.split("\n")

for each_line in passwd_list:
  user_split = each_line.split(":")
  if "#" in user_split[0]:
    continue
  if int(user_split[2]) > 200:
    print("the username %s is greater than 200 of its Uid" % user_split[0])
