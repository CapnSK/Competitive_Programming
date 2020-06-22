for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	mod1,mod0=0,0
	for i in arr:
		if i&1:
			mod1+=1
		else:
			mod0+=1
	if mod1>0:
		if mod0>0:
			print("NO")
		else:
			print("YES")
	else:
		print("YES")