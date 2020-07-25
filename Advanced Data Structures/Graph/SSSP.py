'''
	This is the code for single source shortest path from source node 0 to other n-1 nodes.
	Note: Graph is undirected and unweighted.
'''
def bfs(source,ad_list,V,E):
	visited = [False for i in range(V)]
	dist = [float('inf') for i in range(V)]
	dist[source]=0
	Q = []
	Q.append(source)
	visited[source] = True

	while len(Q)>0:
		node = Q.pop(0)
		for neighbour in ad_list[node]:
			if not visited[neighbour]:
				dist[neighbour] = min(dist[node] + 1,dist[neighbour])
				Q.append(neighbour)
				visited[neighbour] = True


	for i in range(V):
		print(i,"->",dist[i])

V,E = map(int,input().split())
Edges = [[] for i in range(V)]

for i in range(E):
	u,v = map(int,input().split())
	Edges[u].append(v)
	Edges[v].append(u)

bfs(source = 0,ad_list = Edges,V=V,E=E)