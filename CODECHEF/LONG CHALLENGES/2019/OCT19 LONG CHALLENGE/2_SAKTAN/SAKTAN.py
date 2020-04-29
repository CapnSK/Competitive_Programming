while True:
	try:
		for _ in range(int(input())):
			n,m,q=map(int,input().split())
			arr=[[0 for i in range(m)] for j in range(n)]
			queries = []
			for i in range(q):
				queries.append(list(map(int,input().split())))

			prevanswer=0
			prevInd={}
			for i,j in queries:
				i-=1
				j-=1
				answer=prevanswer
				for k in range(m):
					arr[i][k]+=1
					if arr[i][k]%2 ==1:
						answer+=1
					else:
						answer-=1
				for k in range(n):
					arr[k][j]+=1
					if arr[k][j]%2 ==1:
						answer+=1
					else:
						answer-=1
				#print(*arr,sep="\n")
				prevanswer=answer
			print(answer)
				

	except:
		raise