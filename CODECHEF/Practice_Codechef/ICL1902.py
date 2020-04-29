import math
while True:
	try:
		for _ in range(int(input())):
			n=int(input())
			start=int(math.sqrt(n))**2
			remainder = n-start
			count=1
			while remainder != 0:
				temp = int(math.sqrt(remainder))**2
				remainder -= temp
				count+=1
			print(count)

	except (ValueError,EOFError) as e:
		break