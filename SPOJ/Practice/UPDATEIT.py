def update(BIT,index,val,n):
	while index<=n:
		BIT[index]+=val
		index+=(index&-index)
	return

def query(BIT,index,n,debug):
	ans = 0
	while index>0:
		ans+=BIT[index]
		if debug:
			print("index",index,"Answer",ans)
		index-=(index&-index)
	return ans




debug=False
for _ in range(int(input())):
	n,u = map(int,input().split())
	BIT = [0]*(n+1)
	for i in range(u):
		l,r,v = map(int,input().split())
		l+=1
		r+=1
		if debug:
			print("Before update",BIT[1::])
		update(BIT,l,v,n)
		if debug:
			print("After first update",BIT[1::])
		update(BIT,r+1,-v,n)
		if debug:
			print("After second update",BIT[1::])
	q=int(input())
	for i in range(q):
		idx = int(input())
		idx+=1
		print(query(BIT,idx,n,debug))