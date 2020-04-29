N = 100001
p=1000000007
factorial  = [None] * (N + 1)  
natural  = [None] * (N + 1) 
fact = [None] * (N + 1) 
natural [0] = natural [1] = 1

for i in range(2, N + 1, 1): 
    natural [i] = (natural [p % i] *(p - int(p / i)) % p)
    
factorial [0] = factorial [1] = 1
for i in range(2, N + 1, 1): 
    factorial [i] = (natural [i] *factorial [i - 1]) % p

fact[0] = 1
for i in range(1, N + 1): 
    fact[i] = (fact[i - 1] * i) % p 
def main(debug=False):
	global factorial
	global fact
	for _ in range(int(input())):
		n=int(input())
		a=input().strip()
		b=input().strip()
		nfact=fact[n]

		asetbits=a.count('1')
		bsetbits=b.count('1')

		tmp=asetbits+bsetbits
		if tmp>n:
			tmp=n-abs(n-tmp)

		Max=min(tmp,n)

		Min=abs(asetbits-bsetbits)

		ans=0

		for i in range(Min,Max+1,2):
			ans= (ans+(((fact[n] * factorial [i])% p * factorial [n - i])% p))%p

		print(ans)


main(debug=False)