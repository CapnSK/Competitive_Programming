def main(debug=False):
	for _ in range(int(input())):
		n,m,k=map(int,input().split())
		c=[]
		for i in range(n):
			c.append(list(map(int,input().split())))

		answers=[-1 for i in range(n)]
		visited=[False for i in range(k)]

	
		dp={}
		for i in range(n):
			formats=c[i]
			#repeated={}
			temp={j:[] for j in range(1,m+1)}
			for j in range(k):
				ans=formats[j]
				temp[ans].append(j+1)
			dp[i+1]=sorted(temp.items(),key=lambda x:len(x[1]),reverse=True)
		

		# Max=-1
		# Maxlen=-1
		# MaxAns=-1
		# VisitedFormats={0 for i in range(m)}
		# MaxFormats=[]
		# for i in dp:
		# 	if debug:
		# 			print(len(dp[i][0][1]),Maxlen)
		# 	if len(dp[i][0][1])>Maxlen:
		# 		Maxlen=len(dp[i][0][1])
		# 		MaxFormats=dp[i][0][1]
		# 		MaxAns=dp[i][0][0]
		# 		Max=i
		# 	if debug:
		# 		print("Max",Max)
		# answers[Max-1]=MaxAns
		# VisitedFormats=set(MaxFormats)
		# if debug:
		# 	print("Visited formats before",VisitedFormats)
		# for i in range(n):
		# 	if answers[i]==-1:
		# 		l=dp[i+1]

		# 		if len(VisitedFormats)==k:
		# 			VisitedFormats=set()

		# 		Max=-1
		# 		Maxlen=-1
		# 		MaxAns=-1
		# 		VisitedFormats={0 for i in range(m)}
		# 		MaxFormats=[]
		# 		for j in range(i,n):
		# 			if answers[j]==-1:
		# 			if debug:
		# 					print(len(dp[i][0][1]),Maxlen)
		# 			if len(dp[i][0][1])>Maxlen:
		# 				Maxlen=len(dp[i][0][1])
		# 				MaxFormats=dp[i][0][1]
		# 				MaxAns=dp[i][0][0]
		# 				Max=i
		# 			if debug:
		# 				print("Max",Max)
		# 		answers[Max-1]=MaxAns
		# 		VisitedFormats=set(MaxFormats)

		# 		tmp=set(VisitedFormats)
		# 		tmp1=set(VisitedFormats)
		# 		for answer,repeatedFormats in l:
		# 			tmp=set(VisitedFormats)
		# 			tmp.update(repeatedFormats)
		# 			if debug:
		# 				print("answer,repeatedFormats,tmp",answer,repeatedFormats,tmp)
		# 			if len(tmp)>len(tmp1):
		# 				tmp1=tmp
		# 				answers[i]=answer
		# 			else:
		# 				continue
		# 		VisitedFormats=set(tmp1)
		# 		if debug:
		# 			print("Final VisitedFormats",VisitedFormats)


				
		if debug:
			for question in dp:
				print("Question:",question,"Answers",dp[question])
				





		print(*answers)


while True:
	try:
		main(debug=False)
	except (ValueError,EOFError) as e:
		break