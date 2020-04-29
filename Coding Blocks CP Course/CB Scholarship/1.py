from math import gcd
def div(n):
	i=1
	cnt=0
	if n==1:
		return 1
	while i*i <= n:
		if n%i==0:
			if n//i == i:
				cnt+=1
			else:
				cnt+=2
		i+=1
	return cnt

def f(i,j):
	return div(gcd(i,j))

n=int(input())
ans=0
for i in range(1,n+1):
	for j in range(1,n+1):
		print("for i j",i,j,"ans is",ans,"f(i,j) is",f(i,j))
		ans+=f(i,j)

print(ans)