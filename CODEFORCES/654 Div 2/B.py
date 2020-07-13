for _ in range(int(input())):
	n,r = map(int,input().split())
	if n>r:
		print((r*(r+1))//2)
	else:
		n-=1
		ans = (n*(n+1))//2
		print(ans+1)