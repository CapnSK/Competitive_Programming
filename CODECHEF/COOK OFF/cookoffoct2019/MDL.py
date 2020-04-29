for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	#temp=[i for i in arr]

	while len(arr)>2:
		temp=sorted(arr[0:3])
		arr.pop(arr.index(temp[1]))

	print(*arr)