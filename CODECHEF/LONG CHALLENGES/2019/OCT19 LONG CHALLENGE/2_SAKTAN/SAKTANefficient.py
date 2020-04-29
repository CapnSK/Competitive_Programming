while True:
	try:
		for _ in range(int(input())):
			n,m,q=map(int,input().split())
			arr=[[0 for i in range(m)] for j in range(n)]
			queries = []
			for i in range(q):
				queries.append(list(map(int,input().split())))

			rows={i:0 for i in range(1,n+1)}
			cols={i:0 for i in range(1,m+1)}

			odd1,even1=0,0
			odd2,even2=0,0

			for i,j in queries:
				rows[i]+=1
				cols[j]+=1
			answer=0

			l1=list(rows.values())
			l2=list(cols.values())

			# for i in l1:
			# 	if i%2==1:
			# 		odd1+=1
			# 	else:
			# 		even1+=1
			# for i in l2:
			# 	if i%2==1:
			# 		odd2+=1
			# 	else:
			# 		even2+=1

			answer= odd2*even1 + even2*odd1

			print(answer)
	except:
		raise