'''
	This is a solution for Longest Increasing Subsequence in O(n^2) time using DP.
	In this DP:
	dp[i] represents the LIS till index i including that index in the resulting subsequence.
'''

n = int(input())
arr = list(map(int,input().split()))
dp = [0]*n
dp[0] = 1
for i in range(1,n):
	add = 0
	for j in range(0,i):
		if arr[j]<arr[i]:
			add = max(add,dp[j])
	dp[i] = add+1
print(max(dp))