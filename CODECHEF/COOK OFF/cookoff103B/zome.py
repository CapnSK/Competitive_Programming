#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#
def max2(s,t):
    #s = s[::-1]
    print(s)
    cnt = 0
    while True:
        #print(t in s)
        if t in s:
            ind = s.index(t)
            s = s[0:ind] + s[ind+len(t)::]
            cnt+=1
         #   print(s)
        else:
            break
    return cnt

def maxMoves(s, t):
    # Write your code here
    
    a1 = (max2(s,t))
    a2 = (max2(s[::-1],t))
    return max(a1,a2)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    result = maxMoves(s, t)

    print(result)


