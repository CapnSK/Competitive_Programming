from itertools import permutations
debug=False
for _ in range(int(input())):
	n,k = map(int,input().split())
	s=['a']*n
	i=1
	k1=k
	start=0
	while k1>0:
		k1-=i
		if k1>0:
			start+=i
		i+=1
	s[n-(k-start)]='b'
	#print(start,i)
	s[n-1-(i-1)]='b'
	print(''.join(s))