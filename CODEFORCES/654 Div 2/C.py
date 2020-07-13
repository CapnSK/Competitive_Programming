for _ in range(int(input())):
	a,b,n,m = map(int,input().split())

	if (a+b)<(n+m) or min(a,b)<m:
		print("No")
	else:
		if a>=b:
			b-=m
			if a+b>=n:
				print("Yes")
			else:
				print("No")
		elif b>a:
			a-=m
			if a+b>=n:
				print("Yes")
			else:
				print("No")