from bisect import bisect_left,bisect_right

while True:
	try:
		for _ in range(int(input())):
			n=int(input())
			a = list(map(int,input().split()))
			
			atemp=[[a[i],i] for i in range(n)]
			asortedwithind = sorted(atemp,key=lambda x:x[0])
			asorted = [x for x,i in atemp]


			present = [False for i in range(max(a)+1)]
			presentAtIndices = {}

			for i in a:
				present[i]=True

			for element,index in atemp:
				if element in presentAtIndices:
					presentAtIndices[element].append(index)
				else:
					presentAtIndices[element]=[]
					presentAtIndices[element].append(index)

			print(*atemp)
			print(*asortedwithind)
			print(presentAtIndices)
			#i=0
			maxstarvalue=-1
			for element,ind in atemp:
				tmp = filter(lambda x:x[1]<ind,asortedwithind[bisect_left(asorted,element)::])
				starvalue=0
				for e,i in tmp:
					if e%element==0:
						starvalue+=1
				if starvalue>maxstarvalue:
					maxstarvalue=starvalue

			print(maxstarvalue)

	except (ValueError,EOFError) as e:
		break