def main(debug=False):
	for _ in range(int(input())):
		n=int(input())
		xD={}
		yD={}
		for i in range(4*n -1):
			x,y =map(int,input().split())
			if x not in xD:
				xD[x] = []
			if y not in yD:
				yD[y] = []
			xD[x].append(y)
			yD[y].append(x)
		if debug:
			print("xD",xD)
			print("yD",yD)
		X,Y=0,0
		for x in xD:
			if len(xD[x])&1:
				X=x

		for y in yD:
			if len(yD[y])&1:
				Y=y

		print(X,Y)

while True:
	try:
		main(debug=False)
	except (ValueError,EOFError) as e:
		break