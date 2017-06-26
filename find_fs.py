#! /usr/bin/env python

import commands

mount = commands.getoutput("df -k")

mounts = mount.split("\n")
array_to_check = mounts[1:]
for line in array_to_check:
	new_line = line.replace("%", "").split()

	if int(new_line[4]) > 95:
 		print("the filesystem is %s" % ( new_line[0]) )
    
