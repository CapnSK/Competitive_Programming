import math
#from bisect import bisect_left,bisect_right
def getfactors(n):
	factors=[]
	for i in range(1,int(math.sqrt(n))+1):
		if n%i==0:
			if n//i != i:
				factors.append(i)
				factors.append(n//i)
			else:
				factors.append(i)
	return factors



while True:
	try:
		for _ in range(int(input())):
			n=int(input())
			array = list(map(int,input().split()))

			Factors = {i:getfactors(i) for i in array}
			counts={}
			sv=[]
			for i in range(n):
				factors=Factors[array[i]]
				for key in factors:
					if key in counts:
						counts[key]+=1
					else:
						counts[key]=1
				sv.append(counts[array[i]]-1)

			print(max(sv))


	except (ValueError,EOFError) as e:
		break