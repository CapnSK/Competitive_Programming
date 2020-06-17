'''
This code is for a problem with finding minimum element in the given range with point updates as well as range updates-
without lazy propagation implemented.
'''

# If you get a recursion depth error feel free to update the multiplier, currently it is set to 10^5 .
import sys
sys.setrecursionlimit(sys.getrecursionlimit()*100)

import math


# Function can take any built in value {min,max,sum} or any user defined function. 
# It must take an array of two elements as input and provide a single output
def buildTree(Tree,arr,start,end,nodeIndex,debug,function=min): 
	if start==end:
		Tree[nodeIndex]=arr[start]
		return
	mid=(start+end)//2
	buildTree(Tree,arr,start,mid,2*nodeIndex+1,debug)
	buildTree(Tree,arr,mid+1,end,2*nodeIndex+2,debug)
	Tree[nodeIndex]=function([Tree[2*nodeIndex+1],Tree[2*nodeIndex+2]])
	return


def query(Tree,nodeStart,nodeEnd,queryStart,queryEnd,nodeIndex,debug,function=min):
	#NO OVERLAP
	if queryEnd<nodeStart or queryStart>nodeEnd:
		return float('inf') #change to -inf if the function is max and have some default value for sum.

	#COMPLETE OVERLAP
	if queryStart<=nodeStart and queryEnd>=nodeEnd:
		return Tree[nodeIndex]

	#PARTIAL OVERLAP
	#if queryStart<=nodeEnd or queryEnd>=nodeStart:
	mid=(nodeStart+nodeEnd)//2
	leftChildValue = query(Tree,nodeStart,mid,queryStart,queryEnd,2*nodeIndex+1,debug,function)
	rightChildValue = query(Tree,mid+1,nodeEnd,queryStart,queryEnd,2*nodeIndex+2,debug,function)
	return function([leftChildValue,rightChildValue])


def update(Tree,nodeStart,nodeEnd,arrayIndexToBeUpdated,nodeIndex,updatedValue,debug,function=min):
	if debug:
		print("Current Node",nodeIndex,nodeStart,nodeEnd)
	#NO OVERLAP
	if arrayIndexToBeUpdated<nodeStart or arrayIndexToBeUpdated>nodeEnd:
		return

	#LEAF NODE and COMPLETE OVERLAP
	if nodeStart==nodeEnd and nodeStart==arrayIndexToBeUpdated:
		if debug:
			print("updating",nodeStart,"to",updatedValue)
		Tree[nodeIndex]=updatedValue
		return

	#NON LEAF NODE and PARTIAL OVERLAP
	mid=(nodeStart+nodeEnd)//2
	update(Tree,nodeStart,mid,arrayIndexToBeUpdated,2*nodeIndex+1,updatedValue,debug,function) # update left child recursively
	update(Tree,mid+1,nodeEnd,arrayIndexToBeUpdated,2*nodeIndex+2,updatedValue,debug,function) # update right child recursively

	Tree[nodeIndex]=function([Tree[2*nodeIndex+1],Tree[2*nodeIndex+2]]) # update current node's value based on left child and right child
	return


def updateRange(Tree,nodeStart,nodeEnd,queryStart,queryEnd,nodeIndex,updatedValue,debug,function=min):
	#NO OVERLAP
	if queryEnd<nodeStart or queryStart>nodeEnd:
		return

	#A LEAF NODE in given QUERY RANGE
	if nodeStart==nodeEnd and nodeStart>=queryStart and nodeStart<=queryEnd:
		Tree[nodeIndex] = updatedValue
		return

	#A NON LEAF NODE PARTIALLY/COMPLETELY LYING IN QUERY RANGE
	mid=(nodeStart+nodeEnd)//2
	updateRange(Tree,nodeStart,mid,queryStart,queryEnd,2*nodeIndex+1,updatedValue,debug,function)
	updateRange(Tree,mid+1,nodeEnd,queryStart,queryEnd,2*nodeIndex+2,updatedValue,debug,function)

	Tree[nodeIndex]=function([Tree[2*nodeIndex+1],Tree[2*nodeIndex+2]])
	return


def main(debug=True):
	#Taking input
	n=int(input())
	arr=list(map(int,input().split()))
	assert n==len(arr),'length of array does not match input array size'

	#Building segment Tree
	Tree=[0]*(pow(2, math.ceil(math.log(n,2)+1)) -1)
	buildTree(Tree,arr,0,n-1,0,debug)
	if debug:
		print("ST",Tree)

	#Taking queries and performing appropriate actions
	'''
	Query format:  (Note: startIndex and endIndex are inclusive)
	0 -> Query Range  ***Format***    0 startIndex endIndex
	1 -> Point Update ***Format***    1 arrayIndex updatedValue
	2 -> Range Update ***Format***	  2 startIndex endIndex updatedValue
	'''
	q=int(input())
	for _ in range(q):
		Line=input().split()
		assert len(Line)>0, 'No input provided'
		assert int(Line[0]) in range(0,3),'Invalid query'

		if Line[0]=='0':
			assert len(Line)==3,'Query expects start and end index'
			queryStart,queryEnd=map(int,Line[1::])
			print(query(Tree,0,n-1,queryStart,queryEnd,0,debug))


		elif Line[0]=='1':
			assert len(Line)==3,'Query expects array index and updated value'
			nodeIndex,updatedValue=map(int,Line[1::])
			update(Tree,0,n-1,nodeIndex,0,updatedValue,debug)
			if debug:
				print("ST after updating",Tree)

		elif Line[0]=='2':
			assert len(Line)==4,'Query expects start,end index and updated value'
			startIndex,endIndex,updatedValue=map(int,Line[1::])
			updateRange(Tree,0,n-1,startIndex,endIndex,0,updatedValue,debug)
			if debug:
				print("ST after updating",Tree)


try:
	main(debug=True)
except AssertionError as error:
	print(error)