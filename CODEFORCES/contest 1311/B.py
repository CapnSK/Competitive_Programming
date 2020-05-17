from bisect import bisect_left
output=[]
for _ in range(int(input())):
	n,m=map(int,input().split())
	arr=list(map(int,input().split()))
	pos=list(map(int,input().split()))

	pos_d={}
	for i in pos:
		pos_d[i-1]=True

	i=0
	while i<n:
		if i not in pos_d:
			i+=1
			continue
		j=i
		while j<n and j in pos_d:
			j+=1
		arr[i:j+1]=sorted(arr[i:j+1])
		i=j
		i+=1
		if i>=n-1:
			break
		
	ok=True
	for i in range(0,n-1):
		ok &= arr[i]<=arr[i+1]
	print("YES" if ok else "NO")
#print(*output,sep='\n')