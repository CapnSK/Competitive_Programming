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


debug=False
n = int(input())
arr =[0]+ list(map(int,input().split()))
BIT = [0]*(10**5)


if debug:
	print("BIT is",BIT)

ans=0
for i in range(n,0,-1):
	ans += query(BIT,arr[i]-1,n)
	update(BIT,arr[i],1,n)
print(ans)