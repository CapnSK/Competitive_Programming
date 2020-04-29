def main(debug=False):
	for _ in range(int(input())):
		n,k=map(int,input().split())
		a=list(map(int,input().split()))
		inv=0
		inv1=0
		for i in range(n):
			if debug:
				print("for i:",i)
			cnt=0
			for j in range(i+1,n):
				if debug:
					print("\t for j:",j)
				if a[i]>a[j]:
					if debug:
						print("\t\ta[i] a[j]",a[i],a[j])
					cnt+=1
				elif debug:
					print("\t\t a[i]<a[j]")
			if debug:
				print("\tcnt j>i",cnt)
			inv+= cnt*((k*(k+1))//2)
			if debug:
				print("\tinv for j>i",inv)


			cnt=0
			for j in range(i):
				if a[i]>a[j]:
					if debug:
						print("\t\ta[i] a[j]",a[i],a[j])
					cnt+=1
			inv1+= cnt*(((k-1)*(k))//2)

			if debug:
				print("\tcnt j<i",cnt)
				print("\tinv for j<i",inv1)

		print(inv+inv1)

while True:
	try:
		main(debug=False)
	except (ValueError,EOFError) as e:
		break