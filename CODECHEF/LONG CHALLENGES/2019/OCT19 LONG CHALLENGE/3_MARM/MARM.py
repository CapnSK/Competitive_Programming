while True:
	try:
		for _ in range(int(input())):
			n,k=map(int,input().split())
			arr=list(map(int,input().split()))

			toProcessTimes = k//n
			toProcessUpto  = k%n
			toProcessTimes = toProcessTimes%3

			#print(toProcessTimes,toProcessUpto)
			processedArr={}

			#processedArr[0]=arr            #modulo 0


			temparr=[]
			for i in range((n//2)):
				temparr.append(arr[i]^arr[n-i-1])
			if n%2==0:
				temparr+=arr[((n//2)-1)::-1]
			else:
				temparr+=[0]
				temparr+=arr[((n//2)-1)::-1]
			processedArr[1]=temparr			#modulo 1
			



			tarr=[]
			if n%2==0:
				temparr=temparr[0:n//2]
				tarr=arr[n-1:(n//2)-1:-1]
			else:
				temparr=temparr[0:(n//2)+1]
				tarr=arr[n-1:(n//2):-1]
			temparr= tarr+temparr[::-1]
			processedArr[2]=temparr			#modulo 2


			arr1=processedArr[1]
			if n%2==0:
				temparr=temparr[0:n//2]
				tarr=arr1[n-1:(n//2)-1:-1]

			else:
				temparr=temparr[0:(n//2)+1]
				tarr=arr1[n-1:(n//2):-1]
			temparr= tarr+temparr[::-1]
			processedArr[0]=temparr

			#print(processedArr)

			if k>n:
				if toProcessUpto==0:
					#print("here")
					print(*processedArr[toProcessTimes])
				else:
					#print("there")
					Next = (toProcessTimes+1)%3
					arr1 = processedArr[Next]
					arr2 = processedArr[toProcessTimes]
					#print("Next",Next)

					Output = arr1[:toProcessUpto:]+arr2[toProcessUpto::]
					print(*Output)
			else:
				a=processedArr[1]
				a=a[:k:]+arr[k::]
				print(*a)

	except:
		break