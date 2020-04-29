from itertools import combinations

n,l,r,x = map(int,input().split())
a=list(map(int,input().split()))

c=[]
for i in range(2,n+1):
	c+=list(combinations(a,i))

cnt=0

for t in c:
	m=min(t)
	M=max(t)
	s=sum(t)
	if M-m >=x and (s>=l and s<=r):
		cnt+=1

print(cnt)