import math
import random


def kthsmallest(arr,l,r,k):
	if (k>0 and k <= (r-l+1)) :

		pos=randomPartition(arr,l,r)

		if pos-l == k-1 :
			return arr[pos]
		if pos-l > k-1 :
			return kthsmallest(arr,l,pos-1,k)

		return kthsmallest(arr,pos+1,r,k-pos+l-1)

	return max(a)

def swap(arr,a,b):
	temp = arr[a]
	arr[a]=arr[b]
	arr[b]=temp

def partition(arr,l,r):
	x=arr[r]
	i=l
	for j in range(l,r):
		if(arr[j]<=x):
			swap(arr,i,j)
			i+=1
	swap(arr,i,r)
	return i

def randomPartition(arr,l,r):
	n=r-l+1
	pivot=int(random.random()%n)
	swap(arr,l+pivot,r)
	return partition(arr,l,r)





while True :
	try :
		for _ in range(int(input())):
			n,k=map(int,input().split())
			arr=[0]+list(map(int,input().split()))

			final=0
			for i in range(1,n+1):
				for j in range(i,n+1):
					a=arr[i:j+1:1]
					a=sorted(a)
					m=int(math.ceil(k/(j-i+1)))

					ind=int(math.ceil(k/m))-1
					kth=kthsmallest(a,0,j-i+1,ind)
					print(a,k,m,ind,kth)
					#b=sort(a,ind,n)



					if k<=m :
						mini=a[0] #min(a)
						if a.count(mini) in a:
							final+=1
							#print("if",final)
					else :

						if a.count(a[ind]) in a :
							final+=1
							#print("else",final)

			print(final)


	except  :
		break
