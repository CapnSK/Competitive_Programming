for _ in range(int(input())):
	n,m = map(int,input().split())
	A = list(map(int,input().split()))
	B = list(map(int,input().split()))
	print((len(set(B))+1)*len(set(A)))