for _ in range(int(input())):
	n=int(input())
	arr = list(map(int,input().split()))
	Sum = sum(arr[::2])
	ms,cs=0,0
	for i in range(0,n-n%2,2):
		cs = max(0,cs+arr[i+1]-arr[i])
		ms = max(cs,ms)
	cs=0
	for i in range(1,n-int(n%2==0),2):
		cs = max(0,cs+arr[i]-arr[i+1])
		ms = max(cs,ms)
	print(ms+Sum)