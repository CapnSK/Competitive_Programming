from sys import stdin,stdout

def binary_search(arr,n,key):
	start=0
	end=n-1


	while(start<=end):
		mid=(start+end)//2
		if arr[mid]==key:
			return mid
		elif arr[mid]>key:
			end= mid-1
		elif arr[mid]<key:
			start=mid+1
	return -(mid+1)


for _ in range(int(input())):
	n=int(input())
	A=list(map(int,input().split()))
	B=list(sorted(A))
	C=[0 for _ in range(100007)]

	happy=False

	for i in range(n):
		ind=binary_search(B,n,i+1)
		if ind >= 0 :
			C[A[i]]+=1
		
		if C[A[i]]>=2 :
			happy = True
		if happy :
			break
	if happy:
		print("Truly Happy")
	else :
		print("Poor Chef")
