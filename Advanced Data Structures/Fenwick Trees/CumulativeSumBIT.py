'''
Cumulative Sum BIT/Fenwick Tree is implemented in this code.
Time Complexities:
1. Build -> O(N*logN)
2. Update -> O(logN)
3. Query -> O(logN)
'''

def update(BIT,index,val,n):
	while index<=n:
		BIT[index]+=val
		index+=(index&-index)
	return

def query(BIT,index,n):
	ans = 0
	while index>0:
		ans+=BIT[index]
		index-=(index&-index)
	return ans


def queryRange(BIT,l,r,n):
	lV = query(BIT,l-1,n)
	rV = query(BIT,r,n)
	return rV-lV


debug=eval(input("Debug mode?:"))
n = int(input())
arr =[0]+ list(map(int,input().split()))
BIT = [0]*(n+1)
for i in range(1,n+1):
	update(BIT,i,arr[i],n)

if debug:
	print("BIT is",BIT)


q=int(input())
for i in range(q):
	'''
	Query Format:
	1 l r
	2 idx updatedValue
	'''
	Line = list(map(int,input().split()))
	if Line[0]==1:
		l,r = Line[1::]
		print(queryRange(BIT,l,r,n))
	elif Line[0]==2:
		index,val=Line[1::]
		update(BIT,index,val,n)
		if debug:
			print("Updated BIT",BIT)