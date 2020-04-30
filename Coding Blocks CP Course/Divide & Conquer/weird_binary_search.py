def search(arr,key):
	s=0
	e=len(arr)-1

	while s<=e:
		mid= (s+e)//2
		if arr[mid] == key:
			return mid
		elif arr[s]<=arr[mid]:
			if key>=arr[s] and key<=arr[mid]:
				e=mid-1
			else:
				s=mid+1
		elif arr[mid]<=arr[e]:
			if key>=arr[mid] and key<=arr[e]:
				s=mid+1
			else:
				e=mid-1
	return -1
n=int(input())
arr=[int(input()) for i in range(n)]
key=int(input())
print(search(arr,key))