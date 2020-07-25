'''
	This is code to find out no. of connected components in a forest using iterative dfs.
	Graph has vertices from 0 to V-1 and has E edges.
'''

def dfs(source,ID,Edges,components,debug):
	if debug:
		print("ID",ID)
	stack = []
	stack.append(source)
	components[source] = ID
	while len(stack)>0:
		node = stack.pop()
		if debug:
			print("node",node)
		for child in Edges[node]:
			if components[child]==-1:
				if debug:
					print("\tchild",child)
				components[child]=ID
				stack.append(child)
	if debug:
		print("components after",components)
	return


debug = False


V,E = map(int,input().split())
Edges = [[] for i in range(V)]

for i in range(E):
	u,v = map(int,input().split())
	Edges[u].append(v)
	Edges[v].append(u)

components = [-1 for i in range(V)]
ID=0
while True:
	done = True
	for i in range(V):
		if components[i]==-1:
			done=False
			dfs(i,ID,Edges,components,debug)
			ID+=1
	if done:
		break

print("There are",ID,"connected components")
for i in range(V):
	print("Node",i,"belongs to",components[i],"th component.")