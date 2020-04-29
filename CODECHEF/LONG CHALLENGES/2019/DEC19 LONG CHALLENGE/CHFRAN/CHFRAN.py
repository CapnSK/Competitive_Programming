def main(debug=True):
	for _ in range(int(input())):
		n=int(input())
		lr=[]
		for i in range(n):
			lr.append(list(map(int,input().split())))
		d={}

		for i in range(n):
			l1=lr[i][0]
			r1=lr[i][1]
			for j in range(n):
				l2=lr[j][0]
				r2=lr[j][1]
				

while True:
	try:
		main(debug=False)
	except (ValueError,EOFError) as e:
		break