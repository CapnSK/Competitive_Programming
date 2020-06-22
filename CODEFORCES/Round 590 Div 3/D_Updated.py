debug=False
seperateOutput=True
alphs = {chr(i):{} for i in range(97,97+26)}
s=list(input())
n=len(s)
for i in range(n):
	alphs[s[i]][i]=True
output=[]
if debug:
	print(alphs)
q=int(input())
for i in range(q):
	Line = input().split()
	if Line[0]=='1':
		pos,charToReplace = int(Line[1]),Line[2]
		pos-=1
		alphs[s[pos]][pos] = False
		s[pos] = charToReplace
		alphs[s[pos]][pos] =True
		if debug:
			print("alphs after update",alphs)
	elif Line[0]=='2':
		l,r = int(Line[1]),int(Line[2])
		l-=1
		r-=1
		ans=0
		for char,posDict in alphs.items():
			if len(posDict)==0:
				continue
			if debug:
				print("For",char,posDict)
			for poss,present in posDict.items():
				if debug:
					print("\tcurr poss is",poss,end="    ")
				if poss>=l and poss<=r and present:
					if debug:
						print("And it lies in the range",l,r)
					ans+=1
					break
				elif poss>r:
					break
			if debug:
				print("Final answer after",char,ans)
		if seperateOutput:
			output.append(ans)
		else:
			print(ans)
if seperateOutput:
	print(*output,sep='\n')