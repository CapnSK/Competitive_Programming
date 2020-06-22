def buildTree(ST,s,ss,se,nodeInd,debug):
	if ss==se:
		if debug:
			print("At the node",nodeInd)
		ST[nodeInd]=set([s[ss]])
		return
	mid = (ss+se)//2
	buildTree(ST,s,ss,mid,2*nodeInd+1,debug)
	buildTree(ST,s,mid+1,se,2*nodeInd+2,debug)
	ST[nodeInd] = ST[2*nodeInd+1].copy()
	ST[nodeInd].update(ST[2*nodeInd+2])
	return

def update(ST,pos,updatedChar,ss,se,nodeInd,debug):
	if pos>se or pos<ss:
		return
	if ss==se:
		ST[nodeInd]=set([updatedChar])
		return
	mid = (ss+se)//2
	update(ST,pos,updatedChar,ss,mid,2*nodeInd+1,debug)
	update(ST,pos,updatedChar,mid+1,se,2*nodeInd+2,debug)
	ST[nodeInd] = ST[2*nodeInd+1].copy()
	ST[nodeInd].update(ST[2*nodeInd+2])
	return

def query(ST,ss,se,qs,qe,nodeInd,debug):
	if debug:
		print("At node",nodeInd)
	if ss>qe or se<qs:
		return set()
	if ss>=qs and se<=qe:
		new=ST[nodeInd].copy()
		return new
	mid = (ss+se)//2
	l = query(ST,ss,mid,qs,qe,2*nodeInd+1,debug)
	r = query(ST,mid+1,se,qs,qe,2*nodeInd+2,debug)
	if debug:
		print("l,r",l,r)
	l.update(r)
	return l


debug=False
seperateOutput=True
s=input()
n=len(s)
ST=[0]*(4*n + 1)
output=[]
buildTree(ST,s,0,n-1,0,debug)
if debug:
	print("ST",ST)
q=int(input())
for i in range(q):
	Line = input().split()
	if Line[0]=='1':
		pos,charToReplace = int(Line[1]),Line[2]
		update(ST,pos-1,charToReplace,0,n-1,0,debug)
		if debug:
			print("Updated ST",ST)
	elif Line[0]=='2':
		l,r = int(Line[1]),int(Line[2])
		ans=len(query(ST,0,n-1,l-1,r-1,0,debug))
		if seperateOutput:
			output.append(ans)
		else:
			print(ans)
if seperateOutput:
	print(*output,sep='\n')