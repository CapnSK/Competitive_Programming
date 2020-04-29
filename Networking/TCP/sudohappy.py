def count(arr,start,n):
	i=start
	max1=0
	cnt=0
	first=True
	while(i!=start or first):
		if arr[i]==1 :
			cnt+=1
			if cnt>=max1 :
				max1=cnt
		elif arr[i]==0 :
			if cnt>=max1:
				max1=cnt
			cnt=0
		i=(i+1)%n
		first=False
		if max1>=k:
			max1=k
			break
	return max1



def countall(arr,n,maxrotate):

	limit=0
	if maxrotate>=n:
		limit=n
	else :
		limit=maxrotate
	print("limit",limit)
	start=0
	ans=[0 for _ in range(n)]
	i=0


	while(limit>0):
		c=count(arr,start,n)
		ans[i]=c
		i+=1
		start= (start-1) % n
		limit-=1

	print(ans)
	return ans


n,q,k = map(int,input().split())
arr=list(map(int,input().split()))
queries=input().strip()
c=list(queries).count("!")
print("count",c)
ans=countall(arr,n,c+1)
cnt=0

for qs in range(q):
	if queries[qs]=='!':
		cnt=(cnt+1)%n
	elif queries[qs]== '?' :
		print(ans[cnt])