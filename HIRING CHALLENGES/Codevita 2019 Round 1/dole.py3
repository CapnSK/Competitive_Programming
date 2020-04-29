def calc(n,m):
	
if __name__=="__main__":
	calcPrefix()
	l,L,b,B = [int(input()) for i in range(4)]
	childrenFed =0
	for i in range(b,B):
		childrenFed+= (calc(n,i)-calc(n-1,i))

	print(childrenFed)