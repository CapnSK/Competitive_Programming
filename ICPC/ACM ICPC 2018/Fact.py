for _ in range(int(input())):
	s1=[]
	for i in range(3):
		s1.append(list(map(int,input().split())))
	s1.sort()
	cnt=0
	impossible=False
	
	for x in range(1,3):
		cnt=0
		for y in range(0,3):
			if(s1[x][y]<s1[x-1][y]):
				impossible=True
				break
			if(s1[x][y]==s1[x-1][y]):
				cnt+=1
		if(cnt==3):
			impossible=True
		if impossible:
			print("no")
			break
	if not impossible:
		print("yes")