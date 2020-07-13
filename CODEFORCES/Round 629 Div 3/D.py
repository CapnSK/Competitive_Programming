for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	if arr.count(arr[0])==n:
		print(1)
		print(*[1]*n)
	elif n&1:
		found=False
		prev=arr[0]
		i=1
		ans=[1]
		while i<n:
			if prev==arr[i]:
				found=True
				ans.append(ans[-1])
				break
			else:
				ans.append(1 if ans[-1]==2 else 2)
			prev=arr[i]
			i+=1
		while len(ans)<n:
			ans.append(1 if ans[-1]==2 else 2)
		if not found:
			ans[-1]=3
			if arr[-1]==arr[0]:
				found=True
				ans[-1]=ans[0]
		print(2 if found else 3)
		print(*ans)

	else:	
		print(2)
		print(*[1,2]*(n//2))