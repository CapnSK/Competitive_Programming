import sys
#sys.setrecursionlimit(sys.getrecursionlimit()*100)


def getAns(n,m,edges,debug):
	if debug:
		print("edges",edges)
	visited=[False for i in range(n+1)]
	neighbour=[-1 for i in range(n+1)]
	neighbour[1]=1
	neighbour[2]=2
	visited[1]=True
	visited[2]=True
	stack1=[]
	stack2=[]
	for node in edges[2]:
		if node!=1:
			neighbour[node]=2
			visited[node]=True
			stack1.append(node)
	if debug:
		print("stack1",stack1)

	while len(stack1)>0:
		node=stack1.pop()
		for adjacentNode in edges[node]:
			if adjacentNode not in [1,2] and not visited[adjacentNode]:
				stack2.append(adjacentNode)
				visited[adjacentNode]=True
				neighbour[adjacentNode]=2

	if debug:
		print("stack2",stack2)


	while len(stack2)>0:
		node=stack2.pop()
		if node not in [1,2] and not visited[node]:
			visited[node]=True
			neighbour[node]=2

	if debug:
		print("visited",visited)
		print("neighbour",neighbour)

	ans=[]
	for node in edges[1]:
		if not visited[node] and neighbour[node]==-1:
			ans.append(node)
	return sorted(ans)


def main(debug=False):
	for _ in range(int(input())):
		n,m=map(int,input().split())
		edges=[[] for i in range(n+1)]
		E={}
		for i in range(m):
			u,v=map(int,input().split())
			u,v=min(u,v),max(u,v)
			if (u,v) not in E:
				edges[u].append(v)
				edges[v].append(u)
				E[(u,v)]=1

		ans=getAns(n,m,edges,debug)
		print(*ans if len(ans)>0 else [-1])

main(debug=False)