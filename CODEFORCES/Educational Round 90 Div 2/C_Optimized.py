debug=False
for _ in range(int(input())):
	s=input().strip()
	n=len(s)
	res=0
	posInd=-1
	if s.count('+')>0:
		posInd=s.index('+')
	if posInd==-1:
		print(((n*(n+1))//2)+n)
	else:
		posCount=0
		res=0
		i=1
		prevPosCount=-1
		for i in range(n):
			if debug:
				print("before",i,posCount,res)
			if posCount==0 and (i==0 or prevPosCount<0):
				res+=(i+1)
			else:
				res+=1
			prevPosCount=posCount-1
			if s[i]=='-':
				if i==n-1 and posCount==0:
					res+=n
				posCount=max(posCount-1,0)
			else:
				posCount+=1
			if debug:
				print("After",i,posCount,res)
		print(res)