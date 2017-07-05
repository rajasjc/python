#!/usr/bin/env python

dic_naga = {}
with open('/etc/passwd') as naga:
    for each in naga:
        if each.startswith("#"):
           continue
        username, shell = each.split(":")[0], each.split(":")[-1]
        dic_naga[username] = shell

print( [ username for username, shell in dic_naga.items() ] )
