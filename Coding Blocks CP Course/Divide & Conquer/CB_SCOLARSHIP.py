def possible(studs,n,m,x,y):
	if studs*x <=  (n-studs)*y + m:
		return True
	return False
def getAns(n,m,x,y):
	s=1
	e=n
	ans=-1
	while s<=e:
		mid= (s+e)//2
		poss = possible(mid,n,m,x,y)

		if poss:
			ans=mid
			s=mid+1
		else:
			e=mid-1
	return ans

def main(debug=False):
	n,m,x,y=map(int,input().split())
	if n*x <= m:
		print(n)
	else:
		print(getAns(n,m,x,y))

main(debug=False)