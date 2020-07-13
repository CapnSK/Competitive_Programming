debug=True
for _ in range(int(input())):
	s=input()
	res=0
	init = 0
	while True:
		curr = init
		ok = True
		if debug:
			print("for init",init,"curr",curr,':')
		for i in range(len(s)):
			res+=1
			if s[i] == '+':
				curr+=1
			else:
				curr-=1
			if debug:
				print("\t\ti",i,"s[i]",s[i],"res",res,"curr",curr)
			if curr<0:
				ok=False
				break
		if debug:
			print("\tbreak",ok)
		if ok:
			break
		init+=1
	print(res)