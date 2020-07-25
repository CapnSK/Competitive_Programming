'''
	This is a solution for Longest Increasing Subsequence in O(n*log n) time using DP and Segment Tree.
	
	This is like DP1 approach only. Just we are using Segment tree to find max LIS in the range 0 to i-1 
	instead of looping through all values and adding 1 to that value.
	
	So we maintain a Segment Tree for the DP array and for each i we update the count of that element by 
	finding max LIS in range 0 to i-1.
'''
def query(ST,qs,qe,ss,se,nodeInd,debug):
	#no overlap
	if se<qs or qe<ss:
		#If there is no overlap LIS of length 0 is possible from this node.
		return 0
	
	#complete overlap
	if ss>=qs and se<=qe:
		return ST[nodeInd]

	#partial overlap
	mid = (ss+se)//2
	lVal = query(ST,qs,qe,ss,mid,2*nodeInd+1,debug)
	rVal = query(ST,qs,qe,mid+1,se,2*nodeInd+2,debug)
	return max(lVal,rVal)

def update(ST,arrInd,val,ss,se,nodeInd,debug):
	if ss>arrInd or se<arrInd:
		return
	if ss==se and ss==arrInd:
		ST[nodeInd]=val
		return
	mid = (ss+se)//2
	update(ST,arrInd,val,ss,mid,2*nodeInd+1,debug)
	update(ST,arrInd,val,mid+1,se,2*nodeInd+2,debug)
	ST[nodeInd] = max(ST[2*nodeInd+1],ST[2*nodeInd+2])
	return


debug = eval(input("debug?:"))
n = int(input())
arr = list(map(int,input().split()))
#dp = [0]*n

ST = [0]*(4*n + 1)

sorted_arr = []
for i in range(n):
	sorted_arr.append((i,arr[i]))
sorted_arr.sort(key = lambda x:x[1])
if debug:
	print("sorted_arr",sorted_arr)



for i in range(n):
	index, element = sorted_arr[i]
	Max = query(ST = ST,qs = 0,qe = index-1,ss = 0 ,se = n-1,nodeInd = 0,debug = debug)
	update(ST = ST,arrInd = index , val = Max+1, ss = 0, se = n-1, nodeInd = 0 ,debug = debug)

if debug:
	print("ST",ST)

print(ST[0])