def isGood(hour):
	global l,r
	if hour>=l and hour<=r:
		return 1
	else:
		return 0

debug=False
n,h,l,r = map(int,input().split())
hours = list(map(int,input().split()))

dp = [[float('-inf')]*(n+1) for i in range(n+1)]
dp[0][0]=0
sum=0
for i in range(n):
	sum+=hours[i]
	for j in range(n+1):
		A = dp[i][j] + isGood((sum-j)%h)
		dp[i+1][j] = max(dp[i+1][j],A)
		B = dp[i][j] + isGood((sum-j-1)%h)
		if j<n:
			dp[i+1][j+1] = max(dp[i+1][j+1],B)

print(*dp,sep="\n")
print(max(dp[n]))