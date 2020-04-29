from bisect import bisect_left,bisect_right

smallestPrimes = [0]*10000001

def seive():
	for i in range(1,10000001):
		smallestPrimes[i]=i

	for i in range(4,10000001,2):
		smallestPrimes[i]=2

	for i in range(3,10000,2):
		for j in range(i*i,10000001,i):
			if smallestPrimes[j]==j:
				smallestPrimes[j] = i


def getFactors(num):
	res = {}
	while num != 1:
		factor = smallestPrimes[num]
		if factor in res:
			res[factor]+=1
		else:
			res[factor]=1
		num = num//factor
		while num % factor == 0:
			res[factor]+=1
			num = num // factor

	return res

seive()
while True:
	try:
		for _ in range(int(input())):
			n=int(input())
			a = list(map(int,input().split()))
			
			factors = {x:getFactors(x) for x in a}

			A={}
			sv=[0 for i in range(n)]

			for i in range(n):
				primes= factors[a[i]]
				l = len(primes)
				al = []
				Max=-1
				for prime in primes.keys():
					if prime in A:
						if a[i]<=A[prime][-1] or A[prime][-1]!=prime:
							A[prime].append(a[i])
						Max=max(len(A[prime]),Max)-1
					else:
						A[prime]=[]
						A[prime].append(a[i])
						Max=max(Max,0)

				print("for ",a[i]," A is ",A)
				sv[i]=Max
				print("SV for ",a[i]," is ",Max)
			
			print(A)
			print(max(sv))

	except (ValueError,EOFError) as e:
		raise