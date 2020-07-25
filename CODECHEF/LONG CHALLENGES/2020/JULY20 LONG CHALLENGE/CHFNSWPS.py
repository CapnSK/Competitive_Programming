def main(debug=False):
	for _ in range(int(input())):
		n = int(input())
		A = list(map(int,input().split()))
		B = list(map(int,input().split()))
		A.sort()
		B.sort()
		D = {}
		for i in range(n):
			if A[i] not in D:
				D[A[i]]=0
			if B[i] not in D:
				D[B[i]]=0
			D[A[i]]+=1
			D[B[i]]+=1
		
		possible=True
		for k in D:
			v=D[k]
			if v&1:
				possible=False
				break
			else:
				D[k]=v//2

		if not possible:
			print(-1)
			continue

		D1=D.copy()
		X=[]
		Y=[]
		for i in range(n):
			if A[i] in D1 and D1[A[i]]>0:
				D1[A[i]]-=1
			else:
				X.append(A[i])

		D1=D.copy()
		for i in range(n):
			if B[i] in D1 and D1[B[i]]>0:
				D1[B[i]]-=1
			else:
				Y.append(B[i])

		X.sort()
		Y.sort(reverse=True)
		if debug:
			print("X",X)
			print("Y",Y)

		possible=False
		if len(X)==len(Y):
			possible=True

		if not possible:
			print(-1)
			continue

		M = min(min(A),min(B))
		cost=0
		for i in range(len(X)):
			cost+=min(2*M,min(X[i],Y[i]))
		print(cost)




while True:
	try:
		main(debug=False)
	except (EOFError,ValueError) as e:
		break