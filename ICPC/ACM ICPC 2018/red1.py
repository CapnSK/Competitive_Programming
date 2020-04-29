t=int(input())
while t>0:
	n,k=map(int,input().split())
	a=list(map(int,input().split()))
	i=0
	a.sort()
	while i<n and a[i]<=k:
		i+=1
	for j in range(i,n-1):
		if a[j]>k:
			q=j
			while q<n-1 and a[j]==a[q]:
				q+=1
			if q<n-1:
				d=a[j]-k
				a[j]=k
				a[q]-=d
			if q==n-1 and j<n-2:
				d=a[j]-k
				a[j]=k
				a[j+1]=k

	if min(a[n-1],a[n-2])>k:
		d=a[n-2]-k
		a[n-1]-=d
		a[n-2]=k
	print(sum(a))

	t-=1