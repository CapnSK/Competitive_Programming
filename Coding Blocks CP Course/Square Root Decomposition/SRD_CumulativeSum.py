'''
	This is the code for Sum in range [L,R] queries and update queries
	using Square Root Decomposition Technique. Time Complexity: O(q*sqrt(n))
	q = number of queries
	n =  array length
'''

import math

def build(Blocks,BSize,Arr,ASize):
	for i in range(n):
		element = Arr[i]
		Blocks[i//BSize] += element

def query(Blocks,BSize,Arr,l,r,debug):
	l1 = BSize*math.ceil(l/BSize)
	r1 = BSize*math.floor(r/BSize)
	if r1>l1:
		if debug:
			print("for l,r",l,r,"l1,r1 are",l1,r1)


		start = l1//BSize
		end = r1//BSize 
		ans = 0
		for i in range(start,end):
			ans+=Blocks[i]
		if debug:
			print("ans after adding Perfect Blocks",ans)


		for i in range(l,l1):
			ans+=Arr[i]
		if debug:
			print("ans after adding left subpart",ans)


		for i in range(r1,r+1):
			ans+=Arr[i]
		if debug:
			print("ans after adding right subpart",ans)

		return ans
	else:
		ans=0
		for i in range(l,r+1):
			ans+=Arr[i]
		return ans

def update(Blocks,BSize,Arr,ind,val,debug):
	Blocks[ind//BSize] += (val-Arr[ind])
	Arr[ind] = val
	return

debug = eval(input("debug?: "))
n = int(input("Enter Array Size: "))
arr = list(map(int,input("Enter array elements:\n").split()))
block_size = int(math.sqrt(n))
if debug:
	print("Block size",block_size)
Blocks = [0 for i in range(math.ceil(n/block_size))]
build(Blocks,block_size,arr,n)
if debug:
	print("Blocks",Blocks)
q = int(input("Enter number of queries: "))
for i in range(q):
	Line = input().split()
	if Line[0]=='1':
		l,r = map(int,Line[1::])
		print(query(Blocks,block_size,arr,l,r,debug))
	elif Line[0]=='2':
		ind,val = map(int,Line[1::])
		update(Blocks,block_size,arr,ind,val,debug)
		if debug:
			print("arr after update",arr)
			print("Blocks after update",Blocks)
