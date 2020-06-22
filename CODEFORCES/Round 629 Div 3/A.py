debug=False
for _ in range(int(input())):
	a,b=map(int,input().split())
	rem = a%b
	print((b-rem)%b)