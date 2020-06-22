import sys
sys.setrecursionlimit(10000000)
def getWays(ans,hours,ind,totalPassedHours,n,h,l,r):
	if ind>=n:
		return 0
	if ind == n-1:
		thp1 = (hours[ind]+totalPassedHours)%h
		thp2 = (hours[ind]-1+totalPassedHours)%h
		if (thp1>=l and thp1<=r) or (thp2>=l and thp2<=r):
			ans+=1
		return ans
	thp1 = (totalPassedHours+hours[ind])%h
	thp2 = (totalPassedHours+hours[ind]-1)%h
	ans1,ans2 = 0,0
	if thp1>=l and thp1<=r:
		ans1 = getWays(ans+1,hours,ind+1,thp1,n,h,l,r)
	else:
		ans1 = getWays(ans,hours,ind+1,thp1,n,h,l,r)
	if thp2>=l and thp2<=r:
		ans2 = getWays(ans+1,hours,ind+1,thp2,n,h,l,r)
	else:
		ans2 = getWays(ans,hours,ind+1,thp2,n,h,l,r)
	return max(ans1,ans2)

n,h,l,r = map(int,input().split())
hours = list(map(int,input().split()))
print(getWays(0,hours,0,0,n,h,l,r))