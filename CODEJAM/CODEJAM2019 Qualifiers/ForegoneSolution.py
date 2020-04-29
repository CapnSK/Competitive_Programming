for _ in range(int(input())):
	num=input().strip()
	n=int(num)
	diff=[]
	n_diff=[]
	for x in num :
		if x=='4':
			n_diff.append('3')
			diff.append('1')
		else :
			n_diff.append(x)
			diff.append('0')
	#differnce=int(''.join(diff))
	print("Case #",_+1,":",sep="",end=" ")
	print(''.join(n_diff),''.join(diff))
