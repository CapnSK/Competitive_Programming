debug=False
for _ in range(int(input())):
	n = int(input())
	arr = list(map(int,input().split()))
	dp = [[0]*(3) for i in range(n+1)] 
	for i in range(n):
		dp[i+1][0] = max(dp[i+1][0],dp[i][0] + (0 if i&1 else arr[i]))
		if i+2 <=n:
			dp[i+2][1] = max(dp[i+2][1],max(dp[i][0],dp[i][1]) + (arr[i] if i&1 else arr[i+1]))
		dp[i+1][2] = max(dp[i+1][2],max(dp[i][0],dp[i][1],dp[i][2]) + (0 if i&1 else arr[i]))
	print(max(dp[n]))