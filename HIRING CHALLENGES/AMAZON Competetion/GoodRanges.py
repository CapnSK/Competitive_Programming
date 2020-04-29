n,m=map(int,input().split())
A=[]
size=0
for _ in range(m):
	A.append(int(input()))
	size+=1
	A.sort()
	op=0
	for i in range(size):
		rangel=0
		rangeu=0
		if i==0:
			rangel=1
			if i+1 < size :
				rangeu=A[i+1]-1
			else:
				rangeu=n
		elif i==size-1:
			rangeu=n
			if i-1 >= 0 :
				rangel=A[i-1]+1
			else:
				rangel=1
		else :
			rangel=A[i-1]+1
			rangeu=A[i+1]-1
		#print(A[i],rangel,rangeu)
		op+= (rangel+rangeu)
	print(op)


