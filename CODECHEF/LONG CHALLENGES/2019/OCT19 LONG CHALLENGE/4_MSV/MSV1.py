from bisect import bisect_left,bisect_right
import math
while True:
	try:
		for _ in range(int(input())):
			n=int(input())
			a = list(map(int,input().split()))
			
			atemp=[[a[i],i] for i in range(n)]
			asortedwithind = sorted(atemp,key=lambda x:x[0])
			asorted = [x for x,i in asortedwithind]


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

			# print(atemp)
			# print(present)
			# print(presentAtIndices)
			Max = max(a)
			maxstarvalue=-1
			for element,index in asortedwithind:
				currstarvalue=0
				# for i in range(element,max(a)+1,element):
				# 	if present[i]:
				# 		pInd = presentAtIndices[i]
				# 		currstarvalue+=bisect_left(pInd,index)

				nextEl = element
				maxIter=0
				#print("Finding max value of ",element," : ")
				while nextEl<Max+1:
					#print("Next element",nextEl)
					if present[nextEl]:
						currstarvalue+=bisect_left(presentAtIndices[nextEl],index)
					
					NextInd = bisect_right(asorted,nextEl)
					if NextInd<n:
						nextEl = math.ceil(asorted[NextInd]/element)*element
					else:
						break

					maxIter+=1
					if maxIter>index:
						break
				#print("SV for ",element," is ", currstarvalue)
				if currstarvalue>maxstarvalue:
					maxstarvalue=currstarvalue

			print(maxstarvalue)

	except (ValueError,EOFError) as e:
		break