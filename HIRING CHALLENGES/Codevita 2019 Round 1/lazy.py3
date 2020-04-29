def nCr(n, r):
    return (fact(n) / (fact(r) * fact(n - r))) 

def fact(n):
    res = 1 
    for i in range(2, n+1): 
        res = res * i      
    return res

def minv(a, m) : 
    m0 = m 
    y = 0
    x = 1
    if (m == 1) : 
        return 0
    while (a > 1) :
        # q is quotient 
        q = a // m
        t = m 
        # m is remainder now, process 
        # same as Euclid's algo 
        m = a % m 
        a = t 
        t = y
        # Update x and y 
        y = x - q * y 
        x = t 
    # Make x positive 
    if (x < 0) : 
        x = x + m0 
  
    return x

test=int(input())
for _ in range(test):
	n,t,m = map(int,input().split())
	p=nCr(n-t,m)
	q=nCr(n,m)

	mod= 1000000007
	#print(p,q)
	ans=(q-p)*minv(q,mod) % mod
	print(int(ans),end='')
	if _ == test-1:
		break
	print()