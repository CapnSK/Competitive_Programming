while True:
	try:
		
		AdList = {}
		levelwiseNodeList={}
		levelOfEachNode = [-1 for i in range(n)]
		Visited=[False for i in range(n)]
		n,q = map(int,input().split())

		for i in range(n-1):
			x,y = map(int,input().split())
			x,y=min(x,y),max(x,y)
			if x in AdList:
				AdList[x].append(y)
			else:
				AdList[x]=[y]

			if y in AdList:
				AdList[y].append(x)
			else:
				AdList[y]=[x]

		#print(AdList)
		bacteriaCount=list(map(int,input().split()))
		temp=AdList[1]
		Visited[0] = True
		levelOfEachNode[0]=0
		levelwiseNodeList[0]=[1]
		first = True

		currlevel=0
		while len(temp)!=0:
			currlevel+=1
			l=[]
			if first:
				l=AdList[1]
				levelwiseNodeList[1]=l
				for t in l:
					levelOfEachNode[t]=currlevel
			else:
				pass
			for node in temp:

		for i in range(q):
			tmp = input().split()
			# Traverse Down :

			# perform operation


	except (EOFError,ValueError) as e:
		break