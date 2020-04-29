from math import gcd
def mod(a,m):
	ans=0
	for i in a:
		ans*=10
		ans=(ans+int(i))%m
		#print(ans)
	return ans

n,m=input().strip().split()
n=int(n)
m=mod(m,n)
print(gcd(m,n))