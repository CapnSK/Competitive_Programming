for _ in range(int(input())):
	s=input()
	stack=[]
	count=0
	for i in s:
		if i=='1':
			if len(stack)>0 and stack[-1]!='1':
				count+=1
				stack.pop()
			else:
				stack.append(i)
		elif i=='0':
			if len(stack)>0 and stack[-1]!='0':
				count+=1
				stack.pop()
			else:
				stack.append(i)
	print('DA' if count&1 else 'NET')