from bisect import bisect_left 
from bisect import bisect_right 

def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

primes = prime_sieve((1 << 22))
comp = []
for x in range(4 , (1 << 22)):
	ind = bisect_left(primes,x)
	if ind < len(primes) and primes[ind] != x:
		comp.append(x)


def msb(n):
	cnt=0
	while(n>0):
		cnt+=1
		n=n>>1
	return cnt
t=int(input())
#print(bin(10**6))
while t>0:
	n=int(input())
	ms=msb(n)-1
	a,b,c,d=0,0,0,0	
	ind = bisect_right(primes,(n))
	a = primes[ind]
	if (a^n) >= n:
	    a = -1
	ind1 = bisect_right(primes, (1 << (ms + 1)))
	print()
	b = primes[ind1]
	if (b^n) <= n:
	    b = -1

	ind = bisect_right(comp,n)
	c = comp[ind]
	if (c^n) >= n:
	    c = -1
	ind = bisect_left(comp , (1 << (ms + 1)))
	d = comp[ind]
	if (d^n) <= n:
	    d = -1
	print(a,b,c,d)
	t-=1