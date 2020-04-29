for _ in range(int(input())):
	Hero=input()
	output=[]
	cnt=0
	thanos=list("thanos")
	PrevinThanos=False

	if Hero[0] in thanos:
		PrevinThanos=True
	else :
		PrevinThanos=False

	appended = 1
	n=len(Hero)	

	for char in Hero :
		#print(char,cnt)
		if char in thanos and PrevinThanos :
			cnt+=1
			PrevinThanos=True

		elif char in thanos and not PrevinThanos :
			if cnt!=0 :
				output.append(str(cnt))
			cnt=1
			PrevinThanos=True

		elif char not in thanos and PrevinThanos :
			if cnt!=0 :
				output.append(str(cnt))
			cnt=1
			PrevinThanos=False

		elif char not in thanos and not PrevinThanos :
			cnt+=1
			PrevinThanos=False
		if appended == n :
				output.append(str(cnt))
		appended+=1

	print(''.join(output))
		
