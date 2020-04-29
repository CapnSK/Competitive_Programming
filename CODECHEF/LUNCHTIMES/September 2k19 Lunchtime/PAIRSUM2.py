while True:
	try:
		for _ in range(int(input())):
			n,q = map(int,input().split())
			B = list(map(int,input().split()))
			queries=[]

			for i in range(q):
				queries.append(list(map(int,input().split())))


			B = [((-1)**i)*B[i] for i in range(n-1)]

			C=[]
			C.append(B[0])
			for i in range(1,n-1):
				C.append(C[-1]+B[i])


			for p,q in queries:
				p,q = min(p,q),max(p,q)
				if (q-p)%2==0:
					print("UNKNOWN")
					continue
				if p ==1:
					print(C[q-2])
					continue
				else:
					if p%2 == 1:
						print(C[q-2]-C[p-2])
					else:
						print(C[p-2]-C[q-2])


	except:
		break