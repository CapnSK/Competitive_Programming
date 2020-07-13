debug=False
for _ in range(int(input())):
	n=int(input())
	s=input()
	a=[]
	b=[]
	i=0
	while i<n:
		if s[i]=='0':
			a.append('0')
			b.append('0')
		elif s[i]=='2':
			a.append('1')
			b.append('1')
		elif s[i]=='1':
			a.append('1')
			b.append('0')
			i+=1
			break
		i+=1
	while i<n:
		a.append('0')
		b.append(s[i])
		i+=1
	print(''.join(a),''.join(b),sep="\n")