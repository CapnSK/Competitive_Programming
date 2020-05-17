for _ in range(int(input())):
	n,m=map(int,input().split())
	s=input().strip()
	pos=list(map(int,input().split()))
	freq={chr(i):[] for i in range(97,97+26)}
	ans={chr(i):0 for i in range(97,97+26)}

	for i in range(n):
		freq[s[i]].append(i+1)

	for key in freq:
		indices=freq[key]
		ans[key]+=len(indices)
		