import math
for _ in range(int(input())):
	a,b,c = map(int,input().split())
	ab = a*b
	if ab>c:
		if a<c:
			print(1,b)
		else:
			print(-1,b)
	elif ab<=c:
		print(1,-1)