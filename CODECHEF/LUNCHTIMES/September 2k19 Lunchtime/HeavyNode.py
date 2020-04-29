n,q = map(int,input().split())

edges = [[0 for i in range(n)] for j in range(n)]

for i in range(n-1):
	k,l = map(int,input().split())
	edges[k][l],edges[l][k]=1,1

Si = list(map(int,input().split()))

queries=[]
for i in range(q):
	queries.append(list(map(int,input().split())))

