n,p,q,r = map(int,input().split())
a=list(map(int,input().split()))
pqr=[p,q,r]
mat = [[0 for j in range(n)] for i in range(3)]

for i in range(3):
	for j in range(n):
		if i==0:
			if j==0:
				mat[i][j]=pqr[i]*a[j]
			else:
				mat[i][j] = max(mat[i][j-1],pqr[i]*a[j])
		elif i==1 or i==2:
			if j==0:
				mat[i][j]=mat[i-1][j]+pqr[i]*a[j]
			else:
				mat[i][j]=max(mat[i][j-1],mat[i-1][j]+pqr[i]*a[j])

print(mat[2][n-1])