def main(debug=False):
	for _ in range(int(input())):
		n,k,p=map(int,input().split())
		a=list(map(int,input().split()))

		if k%2==1:
			if p==0:
				print(max(a))
			else:
				print(min(a))
		else:
			ans=-1
			if p==0:
				M=max(a[1:n-2:])
				for j in range(1,n-1):
					ans=max(M,min(a[j-1],a[j+1]))
			else:
				m=min(a[1:n-2:])
				for j in range(1,n-1):
					ans=min(m,max(a[j-1],a[j+1]))
			print(ans)
		
while True:
	try:
		main(debug=False)
	except (ValueError,EOFError) as e:
		break