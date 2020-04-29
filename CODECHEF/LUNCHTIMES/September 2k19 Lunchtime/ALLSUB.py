for _ in range(int(input())):
	s=input().strip()
	r=input().strip()
	possible = True
	sdic={chr(i):0 for i in range(97,123)}
	rdic={chr(i):0 for i in range(97,123)}

	for i in s:
		sdic[i]+=1

	for i in r:
		rdic[i]+=1

	for key in s:
		if sdic[key]>rdic[key]:
			possible=False
			break

	if not possible:
		print("Impossible")
	else:
		output = ''
		output1 = ''
		output2 = ''
		for i in s:
			rdic[i]-=1
		firstChar = s[0]
		l = list(rdic.keys())
		i=97
		while(i<ord(firstChar)):
			output1+=rdic[chr(i)]*chr(i)
			output2+=rdic[chr(i)]*chr(i)
			rdic[chr(i)]=0
			i+=1


		toFind = i
		First = True


		'''
		for j in s:
			if toFind==ord(j):
				continue
			elif toFind>ord(j):
				First = True
			else:
				First = False
		'''
		#if First:
		output1+=rdic[chr(i)]*chr(i)
		output1+=s
		
		output2+=s
		output2+=rdic[chr(i)]*chr(i)
		rdic[chr(i)]=0

		output=min(output1,output2)
		
		for key in rdic:
			tmp = rdic[key]*key
			output+=tmp
		print(output)