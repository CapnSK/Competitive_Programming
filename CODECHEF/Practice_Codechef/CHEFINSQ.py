from math import factorial

while True:
	try:
		for _ in range(int(input())):
			n,k = map(int,input().split())
			a= list(map(int,input().split()))

			a.sort()

			freq = {}

			for i in a:
				if i in freq:
					freq[i]+=1
				else:
					freq[i]=1

			answer = 0
			#print(freq.items())
			temp = list(freq.items())
			l = temp[0][1]
			if l > k:
				answer = factorial(l) // (factorial(k)*factorial(l-k))
			else:
				cnt=0
				i=0
				while(temp[i][0] != a[k-1]):
					cnt+= temp[i][1]
					i+=1

				remainingPlaces = k-cnt

				kcnt = a.count(a[k-1])
				answer = factorial(kcnt) // ((factorial(remainingPlaces))*(factorial(kcnt-remainingPlaces)))

			print(answer)

	except:
		raise