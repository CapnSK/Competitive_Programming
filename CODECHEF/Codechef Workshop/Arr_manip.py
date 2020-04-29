#!/bin/python3
import time
max1,x=0,0
n,k=map(int,input().split())

a=[0 for i in range(n+1)]
prefix=[0 for i in range(n)]
b=[i for i in a]


for i in range(k):
    p,q,sum1=map(int,input().split())
    sum2=sum1
    
    for j in range(p,q+1):
    	b[j]+=sum2
    print("Brute",b[1::])
	


    a[p]+=sum1
    if q+1 <= n :
        a[q+1]-=sum1
    print("Efficient",a[1::])



    prefix[0]=a[1]
    for j in range(1,n):
    	prefix[j]=prefix[j-1]+a[j+1]
    print("Prefix",prefix)



    time.sleep(2)

print(max(prefix))