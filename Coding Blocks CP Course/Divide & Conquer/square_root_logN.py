def squareRoot(n,p):
	s=0
	e=int(n)
	ans=-1
	while s<=e:
		mid=(s+e)//2
		if mid*mid == n:
			return mid
		if mid*mid < n:
			ans=mid
			s=mid+1
		else:
			e=mid-1
	prec=0.1
	for i in range(p):
		while ans*ans <=n:
			ans+=prec
		ans-= prec
		prec/=10
	return round(ans,p)

n=float(input())
precision=int(input())
print(squareRoot(n,precision))