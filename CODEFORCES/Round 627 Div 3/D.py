debug=False
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[a[i]-b[i] for i in range(n)]
if debug:
	print("c",c)
c.sort()
from bisect import bisect_right
i=n-1
ans=0
while c[i]>0 and i>=0:
	key=-c[i]
	ind = bisect_right(c,key)
	ans += i-ind
	i-=1
print(ans)
