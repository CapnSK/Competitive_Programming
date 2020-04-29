while True:
	try:
		for _ in range(int(input())):
			row,col=map(int,input().strip().split())
			mat=[list(map(int,input().split())) for i in range(row)]
			#print(mat)
			unsafe=False
			#print(mat[1][2])
			for i in range(row):
				for j in range(col):
					if (i==0 and j==0) or (i==0 and j==col-1) or (i==row-1 and j==0) or (i==row-1 and j==col-1):
						if mat[i][j] > 2:
							unsafe=True
							break
					elif j==0 or j==col-1 or i==0 or i==row-1:
						if mat[i][j] > 3:
							unsafe=True
							break
					else:
						if mat[i][j] > 4:
							unsafe = True
							break

			print("unstable" if unsafe else "stable")

	except (EOFError,ValueError) :
		break