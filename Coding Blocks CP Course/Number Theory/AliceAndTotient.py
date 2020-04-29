def precompute():
	Max=1000001
	arr=[-1 for i in range(Max)]
	arr[1]=1
	for i in range(2,Max,2):
		arr[i]=2
	for i in range(3,Max,2):
		if arr[i]==-1:
			arr[i]=i
			for j in range(i*i,Max,i):
				if arr[j]==-1:
					arr[j]=i
	#print(arr[:100:])
	return arr

def getPrimeFactors(n):
	global arr
	pf=[]

	while n>1:
		pf.append(arr[n])
		n=n//arr[n]

	return list(set(pf))

def totient(n):
	arr=getPrimeFactors(n)
	ans=n
	for i in arr:
		ans = (ans-(ans//i))
	return ans

arr=precompute()
for _ in range(int(input())):
	print(totient(int(input())))