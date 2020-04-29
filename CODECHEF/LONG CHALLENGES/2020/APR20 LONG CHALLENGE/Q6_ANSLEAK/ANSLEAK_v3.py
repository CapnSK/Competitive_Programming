def main(debug=False):
	for _ in range(int(input())):
		n,m,k=map(int,input().split())
		c=[]
		for i in range(n):
			c.append(list(map(int,input().split())))

		for i in range(1,n+1):
			print((i%m)+1 , end=' ')
		print()

while True:
	try:
		main(debug=False)
	except (ValueError,EOFError) as e:
		break