#!/bin/python3
max1,x=0,0
n,k=map(int,input().split())
a=[0 for i in range(n+1)]

for i in range(k):
    p,q,sum1=map(int,input().split())
    a[p]+=sum1
    if q+1 <= n :
        a[q+1]-=sum1
    print(a[1::])

prefix=[0 for i in range(n)]
prefix[0]=a[1]
for j in range(1,n):
    prefix[j]=prefix[j-1]+a[j+1]
print(prefix)
print(max(prefix))  
