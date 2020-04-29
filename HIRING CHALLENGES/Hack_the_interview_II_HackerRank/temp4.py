def main(debug=False):
	n,p=map(int,input().split())
	s=input()
	l1,l0=[],[]
	for i in range(n):
		if s[i]=='1':
			l1.append(i)
		else:
			l0.append(i)
	if debug:
		print('l0',l0)
		print('l1',l1)

main(debug=True)