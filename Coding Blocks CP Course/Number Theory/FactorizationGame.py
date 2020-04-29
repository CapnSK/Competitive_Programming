primes=[-1 for i in range(1000001)]
def precompute():
	global primes
	for i in range(2,len(primes),2):
		primes[i]=2
	primes[1]=1
	for i in range(3,len(primes),2):
		if primes[i]==-1:
			primes[i]=i
			for j in range(i*i,len(primes),i):
				if primes[j]==-1:
					primes[j]=i
	return
	
precompute()
def getPFs(n):
	global primes
	if n<2:
		return []
	pfs=[]
	while n>1:
		pfs.append(primes[n])
		n=n//primes[n]
	return pfs

for _ in range(int(input())):
	n=int(input())
	a=list(map(int,input().split()))
	d={}
	for i in a:
		pfs=getPFs(i)
		for key in pfs:
			if key not in d:
				d[key]=0
			d[key]+=1

	print("Mancunian" if sum(list(d.values()))%2==1 else "Liverbird")