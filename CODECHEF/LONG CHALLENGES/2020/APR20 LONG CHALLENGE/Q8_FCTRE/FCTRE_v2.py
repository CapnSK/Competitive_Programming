def main(debug=False):
	precompute()
	MOD=1000000007
	for _ in range(int(input())):
		n=int(input())
		edges=[[] for i in range(n+1)]
		connected={}
		for i in range(n-1):
			u,v=map(int,input().split())
			u,v=min(u,v),max(u,v)
			edges[u].append(v)
			edges[v].append(u)
			connected[(u,v)]=True
		cost=list(map(int,input().split()))
		queries=[]
		q=int(input())
		while q>0:
			q-=1


while True:
	try:
		main(debug=True)
	except (ValueError,EOFError) as e:
		break