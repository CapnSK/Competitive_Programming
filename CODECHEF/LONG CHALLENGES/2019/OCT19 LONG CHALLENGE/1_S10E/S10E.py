while True:
	try:
		for _ in range(int(input())):
			n = int(input())
			prices = list(map(int,input().split()))
			answer=1
			currmin=prices[0]
			currminInd = 0
			for i in range(1,n):
				# if i<6:
				# 	if currmin>prices[i]:
				# 		currmin=prices[i]
				# 		currminInd=i
				# 		answer+=1
				# else:
				if currminInd<i-5:
					currmin=min(prices[i-5:i:])
					currminInd=prices[i-5:i:].index(currmin)
					if currmin>prices[i]:
						currmin=prices[i]
						currminInd=i
						answer+=1

				else:
					if currmin>prices[i]:
						currmin=prices[i]
						currminInd=i
						answer+=1

			print(answer)
	except:
		raise