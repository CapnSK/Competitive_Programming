def main(debug=False):
	for _ in range(int(input())):
		n=int(input())
		if n==1:
			print(1)
			print(1,1)

		elif n&1:
			print(n//2)
			print(3,1,2,n)
			for i in range(4,n,2):
				print(2,i-1,i)
		else:
			print(n//2)
			for i in range(2,n+1,2):
				print(2,i-1,i)


while True:
	try:
		main(debug=False)
	except (ValueError,EOFError) as e:
		break