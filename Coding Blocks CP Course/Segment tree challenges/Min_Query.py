def buildTree(ST,arr,ss,se,nodeIndex,debug=True):
	if ss==se:
		ST[nodeIndex]=arr[ss]
		return
	mid=(ss+se)//2
	buildTree(ST,arr,ss,mid,2*nodeIndex+1,debug)
	buildTree(ST,arr,mid+1,se,2*nodeIndex+2,debug)
	ST[nodeIndex]=min(ST[2*nodeIndex+1],ST[2*nodeIndex+2])
	return

def query(ST,qs,qe,ss,se,nodeIndex,debug):
	if ss>qe or se<qs:
		return float('inf')
	if ss>=qs and se<=qe:
		return ST[nodeIndex]
	mid=(ss+se)//2
	l=query(ST,qs,qe,ss,mid,2*nodeIndex+1,debug)
	r=query(ST,qs,qe,mid+1,se,2*nodeIndex+2,debug)
	return min(l,r)

def update(ST,arrInd,updatedVal,ss,se,nodeIndex,debug):
	if ss>arrInd or se<arrInd:
		return
	if ss==se and ss==arrInd:
		ST[nodeIndex]=updatedVal
		return
	mid=(ss+se)//2
	update(ST,arrInd,updatedVal,ss,mid,2*nodeIndex+1,debug)
	update(ST,arrInd,updatedVal,mid+1,se,2*nodeIndex+2,debug)
	return

import sys
debug=False
n,q = map(int,input().split())
arr = list(map(int,input().split()))
ST = [sys.maxsize]*(4*n +1)
buildTree(ST,arr,0,n-1,0,debug)
if debug:
	print("ST",ST)
for i in range(q):
	Line=list(map(int,input().split()))
	if Line[0]==1:
		l,r=Line[1::]
		print(query(ST,l-1,r-1,0,n-1,0,debug))
	elif Line[0]==2:
		arrInd,updatedVal=Line[1::]
		update(ST,arrInd-1,updatedVal,0,n-1,0,debug)
		if debug:
			print("ST after update",ST)