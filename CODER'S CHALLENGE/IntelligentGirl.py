for _ in range(int(input())):
	S = input()
	lis = [int(i) for i in S]
	cnt = [0 if (i % 2 == 1) else 1 for i in lis]
	fin = [sum(cnt[i+1::]) for i in range(len(S))]
	#print(cnt)
	print(*fin)
