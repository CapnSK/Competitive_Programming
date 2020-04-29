def count(arr,start,n):
	
	last=(start-1)%n
	max1=[0,0]
	cnt=0
	i=start
	#print()
	while(i!=last):
		if arr[i]==1:
			cnt+=1
		elif arr[i]==0:
			if max1[1]<cnt:
				max1[1]=cnt
			cnt=0
		i=(i+1)%n
	
	if arr[i]==1:
		cnt+=1
	if max1[1]<cnt:
		max1[1]=cnt
	if max1[1]>=k:
		max1[1]=k
	return max1[1]


def countall(arr,n):
	start=0
	ans=[0 for _ in range(n)]
	i=0
	first=True
	temp=start

	while(temp!=start or first):
		first=False
		#print(temp)
		c=count(arr,temp,n)
		ans[i]=c

		i+=1
		temp= (temp-1) % n

	return ans


n,q,k = map(int,input().split())
arr=list(map(int,input().split()))
queries=input().strip()

ans=countall(arr,n)
cnt=0
#print(*ans)
for qs in range(q):
	if queries[qs]=='!':
		cnt=(cnt+1)%n
	elif queries[qs]== '?' :
		print(ans[cnt])