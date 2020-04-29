def search(arr, l, r, x):
	
	mid = int(l + (r-l)/2)
	if r>=l :
		if arr[mid] == x:
			return mid

		elif arr[mid] > x:
			return search(arr,l,mid-1,x)

		elif arr[mid] < x:
			return search(arr,mid+1,r,x)

	return -(mid+1)


arr=list(map(int,input().split()))
n=len(arr)
key=int(input("Enter value to search\n"))
print(search(arr,0,n,key))