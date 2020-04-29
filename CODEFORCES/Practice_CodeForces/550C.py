n = input().strip()
nlen = len(n)

dp = [[False for i in range(8)] for j in range(nlen)]

for i in range(nlen):
	for j in range(8):
		dp[i][]