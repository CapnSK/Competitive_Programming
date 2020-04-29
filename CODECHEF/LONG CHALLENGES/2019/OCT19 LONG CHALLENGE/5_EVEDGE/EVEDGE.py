while True:
	try:
		for _ in range(int(input())):
			n,m = map(int,input().split())
			degree={i:0 for i in range(1,n+1)}
			edges={}
			for i in range(m):
				u,v = map(int,input().split())
				degree[u]+=1
				degree[v]+=1
				edges[(u,v)]=1
			if m%2==0:
				print(1)
				print(*[1 for i in range(n)])
			else:
				degrees=list(degree.items())
				OddFound = False
				OddVer=-1
				for v,d in degrees:
					if d%2==1:
						OddFound=True
						OddVer = v
						break
				if OddFound:
					print(2)
					subgroups=[1 for i in range(n)]
					subgroups[OddVer-1]=2
					print(*subgroups)
				else:
					print(3)
					subgroups = [1 for i in range(n)]
					first=-1
					second=-1
					k=list(edges.keys())[0]
					first,second=k
					subgroups[first-1]=2
					subgroups[second-1]=3
					print(*subgroups)
	except (ValueError,EOFError) as e:
		break