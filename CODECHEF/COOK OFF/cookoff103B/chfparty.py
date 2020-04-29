while True :
	try :
		for _ in range(int(input())):
			n=int(input())
			arr=list(map(int,input().split()))
			sorted_arr=sorted(arr)

			cnt=0

			for i in range(n):
				if(sorted_arr[i]<=cnt):
					cnt+=1
			print(cnt)

	except :
		break