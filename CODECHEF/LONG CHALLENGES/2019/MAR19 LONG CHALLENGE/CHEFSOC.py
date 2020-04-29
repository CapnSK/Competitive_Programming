while True :
	#try :
		for _ in range(int(input())):
			n=int(input())
			dogs=list(map(int,input().split()))

			if sum(dogs) == n :
				print(n)
				continue
			



	#except :
	#	break