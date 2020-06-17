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
	if qs>se or qe<ss:
		return
	if ss==se:
		ST[nodeInd] = str(updateTo)*(se-ss +1)
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
buildTree(ST,0,n-1,0,debug)
if debug:
	print("ST",ST)

for i in range(q):
	qtype,l,r = map(int,input().split())
	if qtype in [0,1]:
		update(ST,qtype,l,r,0,n-1,0,debug)
		if debug:
			print("After update",ST)
	elif qtype == 2:
		ans = query(ST,l,r,0,n-1,0,debug)
		print(int(ans,2))
