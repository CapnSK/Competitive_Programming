def buildTree(ST,arr,ss,se,nodeIndex,debug=True):
	if ss==se:
		ST[nodeIndex]=[arr[ss]]
		return
	mid=(ss+se)//2
	buildTree(ST,arr,ss,mid,2*nodeIndex+1,debug)
	buildTree(ST,arr,mid+1,se,2*nodeIndex+2,debug)
	ST[nodeIndex]= []                                #ST[2*nodeIndex+1]+ST[2*nodeIndex+2]
	i,j=0,0
	while i<len(ST[2*nodeIndex+1]) and j<len(ST[2*nodeIndex+2]) :
		if ST[2*nodeIndex+1][i] < ST[2*nodeIndex+2][j]:
			ST[nodeIndex].append(ST[2*nodeIndex+1][i])
			i+=1
		else:
			ST[nodeIndex].append(ST[2*nodeIndex+2][j])
			j+=1

	
	while i<len(ST[2*nodeIndex+1]):
		ST[nodeIndex].append(ST[2*nodeIndex+1][i])
		i+=1

	while j<len(ST[2*nodeIndex+2]):
		ST[nodeIndex].append(ST[2*nodeIndex+2][j])
		j+=1

	return


from bisect import bisect_left
def query(ST,qs,qe,ss,se,k,nodeIndex,debug):
	if ss>qe or se<qs:
		return 0
	if ss>=qs and se<=qe:
		return len(ST[nodeIndex])-bisect_left(ST[nodeIndex],k)
	mid=(ss+se)//2
	l=query(ST,qs,qe,ss,mid,k,2*nodeIndex+1,debug)
	r=query(ST,qs,qe,mid+1,se,k,2*nodeIndex+2,debug)
	return l+r

# def update(ST,arrInd,updatedVal,ss,se,nodeIndex,debug):
# 	if ss>arrInd or se<arrInd:
# 		return
# 	if ss==se and ss==arrInd:
# 		ST[nodeIndex]=updatedVal
# 		return
# 	mid=(ss+se)//2
# 	update(ST,arrInd,updatedVal,ss,mid,2*nodeIndex+1,debug)
# 	update(ST,arrInd,updatedVal,mid+1,se,2*nodeIndex+2,debug)
# 	return

import sys
debug=False
n = int(input())
arr = list(map(int,input().split()))
ST = [-sys.maxsize]*(4*n +1)
buildTree(ST,arr,0,n-1,0,debug)
if debug:
	print("ST",ST)
q = int(input())
for i in range(q):
	l,r,k=map(int,input().split())
	print(query(ST,l-1,r-1,0,n-1,k,0,debug))