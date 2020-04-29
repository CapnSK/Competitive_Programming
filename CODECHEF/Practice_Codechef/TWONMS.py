while True:
	try:
		for _ in range(int(input())):
			a,b,n=map(int,input().split())
			if n%2 == 0 :
				if a >= b:
					print(a//b)
				else:
					print(b//a)
			else:
				a2=2*a
				if a2 >= b:
					print(a2//b)
				else:
					print(b//a2)

	except (EOFError,ValueError):
		break