def main(debug=False):
	for _ in range(int(input())):
		n,m=map(int,input().split())
		a=[int(input()) for i in range(n)]
		if n==0 and m==0:
			print("Yes")
			continue
		if n==0:
			print("No")
			continue
		if m==0:
			print("Yes")
			continue
		for i in range(1,1<<(n+1)):
			b=bin(i)[2::].rjust(n,"0")

			s=0
			if debug:
				print(b)
			for j in range(len(b)):
				#j=int(j)
				if debug:
					print(a[j],b[j])
				if b[j]=='1':
					s+=(a[j])
			if debug:
				print(s,"\n\n")
			if s==m:
				print("Yes")
				break
			if i==1<<(n+1) -1:
				print("No")
				break

while True:
	try:	
		main(debug=False)
	except ValueError:
		break