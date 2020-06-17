#incomplete code xD
def buildTree(ST,ss,se,nodeInd,debug):
	if ss==se:
		ST[nodeInd] = '0'
		return
	mid = (ss+se)//2
	buildTree(ST,ss,mid,2*nodeInd+1,debug)
	buildTree(ST,mid+1,se,2*nodeInd+2,debug)
	ST[nodeInd] = ST[2*nodeInd+1] + ST[2*nodeInd+2]
	return

def update(ST,updateTo,qs,qe,ss,se,nodeInd,debug):
	if Lazy[nodeInd] != ' ':
		ST[nodeInd] = bin(int(Lazy[nodeInd],2) | int(ST[nodeInd]))[2::]
		Lazy[nodeInd] = ' '
		if ss!=se:
			mid = (ss+se)//2
			Lazy[2*nodeInd+1] = bin(int(ST[nodeInd][ss:mid+1]))[2::]
			Lazy[2*nodeInd+2] = bin(int(ST[nodeInd][mid+1::]))[2::]
	if qs>se or qe<ss:
		return
	if ss>=qs and se<=qe:
		ST[nodeInd] = str(updateTo)*(se-ss +1)
		if ss!=se:
			mid = (ss+se)//2
			ST[2*nodeInd+1] = str(updateTo)*(mid-ss +1)
			ST[2*nodeInd+2] = str(updateTo)*(se-mid +1)
		return
	mid = (ss+se)//2
	update(ST,updateTo,qs,qe,ss,mid,2*nodeInd+1,debug)
	update(ST,updateTo,qs,qe,mid+1,se,2*nodeInd+2,debug)
	ST[nodeInd] = ST[2*nodeInd+1] + ST[2*nodeInd+2]
	return

def query(ST,qs,qe,ss,se,nodeInd,debug):
	if qs>se or qe<ss:
		return ''
	if ss>=qs and se<=qe:
		return ST[nodeInd]
	mid = (ss+se)//2
	l = query(ST,qs,qe,ss,mid,2*nodeInd+1,debug)
	r = query(ST,qs,qe,mid+1,se,2*nodeInd+2,debug)
	return l+r


debug = False
n,q = map(int,input().split())
ST = [' ']*(4*n + 1)
Lazy = [' ']*(4*n + 1)
buildTree(ST,0,n-1,0,debug)
if debug:
	print("ST",ST)
	print("Lazy",Lazy)

for i in range(q):
	qtype,l,r = map(int,input().split())
	if qtype in [0,1]:
		update(ST,qtype,l,r,0,n-1,0,debug)
		if debug:
			print("After update ST",ST)
			print("After update Lazy",Lazy)
	elif qtype == 2:
		ans = query(ST,l,r,0,n-1,0,debug)
		print(int(ans,2))
