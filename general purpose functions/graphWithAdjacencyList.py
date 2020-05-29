def main(debug=False):
	n,m=map(int,input().split()) # n is no. of vertices from 1 to n and m is no. of edges
	edges={}
	adjacencyMatrix=[[0 for i in range(n)] for i in range(n)]
	for i in range(m):
		u,v=map(int,input().split())
		if u not in edges:
			edges[u]=[]
		if v not in edges:
			edges[v]=[]
		edges[u].append(v)
		edges[v].append(u)
		#print("before",*adjacencyMatrix,sep='\n')
		adjacencyMatrix[u-1][v-1]=1
		adjacencyMatrix[v-1][u-1]=1
		#print("afer",*adjacencyMatrix,sep='\n')

	for vertex,neighbourVertices in edges.items():
		print(vertex,"is connected to these",neighbourVertices," vertices.")

	print(*adjacencyMatrix,sep='\n')


while True:
	try:
		main(debug=False)
	except (ValueError,EOFError) as e:
		break