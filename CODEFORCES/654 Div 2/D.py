debug=False
for _ in range(int(input())):
	n,k = map(int,input().split())
	mat = [[0]*(n+1) for i in range(n+1)]
	p,q=0,0
	while k>0:
		mat[p+1][q+1]=1
		p+=1
		q+=1
		q%=n
		if p==n:
			p=0
			q+=1
			q%=n
		k-=1
	
	
	if debug:
		print("After i j k",i,j,k)
	
	MaxR,MinR,MaxC,MinC = 0,float('inf'),0,float('inf')
	for i in range(1,n+1):
		SumR,SumC=0,0
		for j in range(1,n+1):
			SumR+=mat[i][j]
			SumC+=mat[j][i]
		MinR=min(MinR,SumR)
		MinC=min(MinC,SumC)
		MaxR=max(MaxR,SumR)
		MaxC=max(MaxC,SumC)
	if debug:
		print(MaxC,MinC,MaxR,MinR)
	print((MaxC-MinC)**2+(MaxR-MinR)**2)
	for l in range(1,n+1):
		print(*mat[l][1::],sep="")