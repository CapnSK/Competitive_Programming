while True:
	try :
		for _ in range(int(input())):
			n=int(input())
			students=list(map(int,input().split()))
			jars=0
			for i in students:
				jars+=(i-1)
			jars+=1
			print(jars)
			
	except : 
		break