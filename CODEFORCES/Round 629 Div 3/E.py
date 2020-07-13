# This code gives WA.

def dfs1(source,dest,debug):
	temp = dest
	path = []
	while temp != 1:
		path.append(temp)
		temp = parent[temp]
	path.append(1)
	return path[::-1]
def dfs(node,debug):
	global E,n,parent,depth
	visited = [False for i in range(n+1)]
	stack = [1]
	while len(stack)>0:
		node = stack.pop()
		if debug:
			print("Current node",node)
		if not visited[node]:
			for child in E[node]:
				if visited[child]:
					continue
				if debug:
					print("\tcurrent child",child)
				parent[child] = node
				depth[child] = depth[node] + 1
				stack.append(child)
			if debug:
				print("Stack after",stack)
			visited[node]=True
	if debug:
		print("Node:   ",*[i for i in range(1,n+1)])
		print("Parent:",*parent[1::])
		print("Depth:  ",*depth[1::])


debug=False
n,m = map(int,input().split())
E = [[] for i in range(n+1)]
for i in range(n-1):
	u,v = map(int,input().split())
	u,v = min(u,v),max(u,v)
	E[u].append(v)
	E[v].append(u)
if debug:
	print("Edges",E)

parent = [-1 for i in range(n+1)]
depth = [-1 for i in range(n+1)]
depth[1] = 0
dfs(1,debug)

for i in range(m):
	nodes = list(map(int,input().split()))
	deepestNode=-1
	deepestNodeDepth=-1
	for node in nodes:
		if depth[node]>deepestNodeDepth:
			deepestNodeDepth=depth[node]
			deepestNode=node
	if debug:
		print("deepestNode",deepestNode,"deepestNodeDepth",deepestNodeDepth)

	l=len(nodes)
	nodeD={i:False for i in range(1,n+1)}
	path = dfs1(1,deepestNode,debug)
	if debug:
		print("Path", path)
	for node in path:
		nodeD[node] = True
	poss=True
	for node in nodes:
		if node in path or parent[node] in path:
			continue
		else:
			poss=False
	print("YES" if poss else "NO")