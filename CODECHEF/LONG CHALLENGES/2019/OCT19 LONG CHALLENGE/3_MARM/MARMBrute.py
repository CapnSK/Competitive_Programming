for _ in range(int(input())):
	n,k=map(int,input().split())
	arr=list(map(int,input().split()))

	for i in range(k):
		ind = i%n
		arr[ind]=arr[ind]^arr[n-ind-1]

	print(*arr)