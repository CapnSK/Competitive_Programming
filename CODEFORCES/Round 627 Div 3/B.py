for _ in range(int(input())):
	n=int(input())
	debug=True
	arr=list(map(int,input().split()))
	d={}
	found=False
	for i in range(n):
		if arr[i] not in d:
			d[arr[i]] = i
		else:
			if i-d[arr[i]]>1:
				found=True
				break
	print("YES" if found else "NO")