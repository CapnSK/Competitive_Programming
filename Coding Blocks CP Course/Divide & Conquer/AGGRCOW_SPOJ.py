def possible(mid,stalls,n,c):
	lastCow=stalls[0]
	i=1
	count=1
	while i<n:
		if stalls[i]-lastCow >= mid:
			count+=1
			lastCow=stalls[i]
		if count==c:
			return True
		i+=1
	return False
def getAns(stalls,n,c):
	s=stalls[0]
	e=stalls[-1]-stalls[0]
	ans=-1
	while(s<=e):
		mid=(s+e)//2
		if possible(mid,stalls,n,c):
			ans=mid
			s=mid+1
		else:
			e=mid-1
	return ans

def main(debug=False):
	for _ in range(int(input())):
		n,c=map(int,input().split())
		stalls=[int(input()) for i in range(n)]
		print(getAns(sorted(stalls),n,c))

main(debug=False)