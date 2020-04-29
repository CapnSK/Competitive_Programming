def main(debug=False):
	for _ in range(int(input())):
		n,m,k=map(int,input().split())
		c=[]
		for i in range(n):
			c.append(list(map(int,input().split())))
		dp={}
		prob={}
		answers=[-1 for i in range(n)]
		for i in range(n):
			questions=c[i]
			if i+1 not in dp:
				dp[i+1]={}
				prob[i+1]={}
			for answer in questions:
				if answer not in dp[i+1]:
					dp[i+1][answer]=0
				dp[i+1][answer]+=1
			maxProb=0
			finalAns=-1
			for q in dp[i+1]:
				a=dp[i+1][q]
				probs=a/float(k)
				prob[i+1][q]=probs
				if probs>maxProb:
					maxProb=probs
					finalAns=q
				if debug:
					print("for q",i+1,"ans :",q,"prob is",probs,"final Ans is",finalAns)
			answers[i]=finalAns
	
		if debug:
			print("dp",dp)
			print("prob",prob)
			print("final answers",answers)

		print(*answers)



while True:
	try:
		main(debug=True)
	except (ValueError,EOFError) as e:
		break