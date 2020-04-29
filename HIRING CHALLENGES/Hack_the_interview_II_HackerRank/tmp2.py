import sys
sys.setrecursionlimit(sys.getrecursionlimit()*10)
import math

def build(S,s,e,tree,index,debug):
	if debug:
		print("Building tree for ",index)
	if s==e:
		tree[index]=S[s]
		return

	mid = (s+e)//2
	build(S,s,mid,tree,2*index,debug)
	build(S,mid+1,e,tree,2*index +1,debug)
	tree[index]=max(tree[2*index],tree[2*index +1])
	return

def query(tree,ss,se,qs,qe,index):
	if ss>=qs and se<=qe:
		return tree[index]
	if qe<ss or qs>se:
		return chr(96)
	mid=(ss+se)//2
	l=query(tree,ss,mid,qs,qe,2*index)
	r=query(tree,mid+1,se,qs,qe,2*index +1)
	return max(l,r)


def main(debug=False):
	n=int(input())
	S=input().strip().lower()
	occurences=[{chr(i):0 for i in range(97,97+26)} for i in range(n+1)]
	for i in range(1,n+1):
		occurences[i]=occurences[i-1].copy()
		occurences[i][S[i-1]]+=1
	if debug:
		print(occurences)
	nextPowOf2 = pow(2, math.ceil(math.log(n,2)))
	if debug:
		print("nextPowOf2",nextPowOf2)
	size = 2*nextPowOf2
	tree=['' for i in range(size)]
	build(S,0,n-1,tree,1,debug)
	if debug:
		print(tree)
	q=int(input())
	for _ in range(q):
		qs,qe=map(int,input().split())
		maxChar=query(tree,0,n-1,qs,qe,1)
		if debug:
			print("maxChar",maxChar) 
		print(occurences[qe+1][maxChar]-occurences[qs][maxChar])


main(debug=False)