for _ in range(int(input())):
	a,b=map(int,input().split())
	if a<b:
		if (b-a)&1:
			print(1)
		else:
			print(2)
	elif a==b:
		print(0)
	else:
		if (b-a)&1:
			print(2)
		else:
			print(1)

