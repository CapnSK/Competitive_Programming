#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxScore' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER m
#

def maxScore(a, m):
    a.sort()
    MOD=1000000007
    n=len(a)
    segments=n//m
    j=0
    ans=0
    for i in range(segments-1):
        #print("for")
        k=0
        Sum=0
        while k<m:
            #print("while")
            Sum+=a[j]
            j+=1
            k+=1
        Sum%=MOD
        ans+= Sum*(i+1)
        ans%=MOD
    while j<n:
        ans+= (segments*a[j])%MOD
        j+=1
    return ans%MOD
    
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    ans = maxScore(a, m)
    print(ans)