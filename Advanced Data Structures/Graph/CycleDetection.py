'''
	This is a code to detect a cycle in a connected graph.
'''


def dfs(ad_list,V,E,root,debug):
	stack = [(0,-1)]
	visited = [False for i in range(V)]
	visited[0] = True
	while len(stack)>0:
		node,parent = stack.pop()
		for child in ad_list[node]:
			if not visited[child]:
				visited[child]=True
				stack.append((child,node))
			elif child != parent:
				return True
	return False

debug = False


V,E = map(int,input().split())
'''
	Another simple logic would be for V vertices if there are more than V-1 edges then the graph has to have a cycle, provided that it does not contain 
	parallel edges or self edges.
	below condition would work.
'''

# if E>V-1:
# 	print(True)

Edges = [[] for i in range(V)]

for i in range(E):
	u,v = map(int,input().split())
	Edges[u].append(v)
	Edges[v].append(u)

Cycle = dfs(ad_list = Edges, V=V , E=E , root = 0 , debug = debug)
print("Yes, the graph contains cycle" if Cycle else "No, the graph does not contain cycle")