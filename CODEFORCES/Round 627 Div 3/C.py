for _ in range(int(input())):
	debug=False
	path=input()
	n=len(path)
	path='R'+path+'R'
	prevPos=0
	d=float('-inf')
	for i in range(1,n+2):
		if path[i]=='R':
			if debug:
				print(i)
				print("\t\td before",d)
			d=max(d,i-prevPos)
			if debug:
				print("\t\td after",d)
			prevPos=i
	print(d)
