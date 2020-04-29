def main(debug=False):
	for _ in range(int(input())):
		n=int(input())
		scores = list(map(int,input().split()))
		scores=sorted(scores)
		

		x,y,z=0,0,0

		N=n//4

		x=scores[N]
		y=scores[2*N]
		z=scores[3*N]

		#print(scores)
		if scores[N-1]==x or scores[2*N - 1]==y or scores[3*N - 1]==z:
			print(-1)
		else:
			print(x,y,z)

while True:
	try:
		main(debug=False)
	except (ValueError,EOFError) as e:
		break