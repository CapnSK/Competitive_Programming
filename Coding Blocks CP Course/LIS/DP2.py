'''
	This is a solution for Longest Increasing Subsequence in O(n*log n) time using DP.
	In this DP:
		dp[i] represents LIS of length i with max element as dp[i].
'''

from bisect import bisect_left,bisect_right


n = int(input())
arr = list(map(int,input().split()))
dp = [float('inf')]*(n+1)
dp[0] = float('-inf')

for i in range(n):
	element = arr[i]
	index = bisect_right(dp,element)
	if index<n+1:
		dp[index] = min(dp[index],element)

print(dp)
count=0
for i in dp:
	if i not in [float('inf'),float('-inf')]:
		count+=1
print(count)