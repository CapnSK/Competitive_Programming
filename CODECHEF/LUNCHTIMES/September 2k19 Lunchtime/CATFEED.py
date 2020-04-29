while True:
	try:
		for _ in range(int(input())):
			n,m = map(int,input().split())
			serves = list(map(int,input().split()))
			i=0
			j=min(n,m)
			possible = True
			g=0
			first = True
			while i<m:
				freq = {}
				for k in range(1,n+1):
					freq[k]=0
				for k in range(i,j):
					key = serves[k]
					freq[key]+=1

				M = max(list(freq.values()))
				m1 = min(list(freq.values()))

				if M-m1 >1:
					possible = False
					break
				else:
					i = j
					j = min((j+n),m)
				g+=1
				if j == m-1 and first:
					first = False
				elif j == m-1 and not first:
					break
			if possible:
				print("YES")
			else:
				print("NO")
	except:
		break