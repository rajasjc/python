#!/usr/bin/env python
import random

number_of_head_needed = 10
number_of_head_now = 0
total_attempt = 0

while number_of_head_now < number_of_head_needed:
    toss = random.randint(0, 1)
    total_attempt += 1

    if toss == 0:
      number_of_head_now += 1
    
    else:
      number_of_head_now = 0

print("the total number of attemt is %s to get number of head %s" % (total_attempt, number_of_head_now))
      
