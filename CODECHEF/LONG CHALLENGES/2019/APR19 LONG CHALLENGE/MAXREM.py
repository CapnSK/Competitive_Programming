while True :
	try :
		n=int(input())
		arr=list(map(int,input().split()))
		sorted_arr = sorted(list(set(arr)))
		#print(arr,sorted_arr)
		print(sorted_arr[-2])
	except :
		break