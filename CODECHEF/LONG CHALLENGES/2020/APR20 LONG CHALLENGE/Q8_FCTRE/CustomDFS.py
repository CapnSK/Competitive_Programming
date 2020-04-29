def dfs(visited,u,v,stack):
	stack.append(u)
	if u==v:
		visited[v]=True
		return [True,stack]
	visited[v]=True
	flag=0
	if len(V[u])>0:
		found=False
		for j in V[u]:
			if visited[j]==False:
				found,path=dfs(visited,j,v,stack)
				if found:
					flag==1
					stack.clear()
					for i in path:
						stack.append(i)
					return [True,stack]
	if flag==0:
		del stack[-1]
		return [False,stack]

def call(u,v,n,stack):
	visited=[0 for i in range(n+1)]
	found,path=dfs(visited,u,v,stack)
	return path

 
 
def addEdge(x, y): 
    V[x].append(y) 
    V[y].append(x) 



n = int(input())

V = [[] for i in range(n+1)]
stack = [] 
for i in range(n-1):
    k,l=map(int,input().split())
    addEdge(k,l)

print(call(int(input()),int(input()),n,stack))