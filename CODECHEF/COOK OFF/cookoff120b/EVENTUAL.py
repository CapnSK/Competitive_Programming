def main(debug=False):
	for _ in range(int(input())):
		n=int(input())
		s=input().strip()
		d={chr(i):0 for i in range(97,97+26)}
		if n&1:
			print("NO")
			continue
		for i in s:
			d[i]+=1

		poss = True
		for k in d:
			if d[k]&1:
				poss=False
				break

		print("YES" if poss else "NO")
while True:
	try:
		main(debug=False)
	except (EOFError,ValueError) as e:
		break