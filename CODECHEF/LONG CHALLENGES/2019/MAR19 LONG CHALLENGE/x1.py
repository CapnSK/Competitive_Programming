import math

while True :
	try :
		for _ in range(int(input())):
			n,k=map(int,input().split())
			arr=[0]+list(map(int,input().split()))

			final=0
			for i in range(1,n+1):
				for j in range(i,n+1):
					a=arr[i:j+1:1]
					print("a",a,end="  ")
					a=sorted(a)
					m=int(math.ceil(k/(j-i+1)))


					if k<=m :
						if a.count(a[0]) in a:
							print(k,m,a[0])
							final+=1
					else :
						ind=int(math.ceil(k/m))-1
						if ind<=j and a.count(a[ind]) in a :
							print(k,m,a[ind])
							final+=1

					print()
			print(final)


	except  :
		break