while True:
	try:
		for _ in range(int(input())):
			n=int(input())
			a = list(map(int,input().split()))
			#dp=[[0 for i in range(j)] for j in range(1,n+1)]

			#print(dp)
			Max=-1
			for i in range(n):
				answer=0
				for j in range(n):
					if j<i:
						if a[j]%a[i]==0:
							answer+=1
					else:
						break
				Max = max(answer,Max)
			print(Max)
	except:
		break