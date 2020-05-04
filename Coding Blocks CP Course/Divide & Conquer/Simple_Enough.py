from math import log,floor

def F(n,s,e,ql,qr,debug):
	if ql>e or qr<s:
		return 0
	if n == 1:
		return 1

	mid = (s+e)//2

	ans = 0
	left = F(n//2,s,mid-1,ql,qr,debug)
	m = n%2
	right = F(n//2,mid+1,e,ql,qr,debug)

	ans+= left + right
	if mid>=ql and mid<=qr:
		ans+=m

	return ans

def main(debug=False):
	n,ql,qr=map(int,input().split())
	nl=0
	nr=pow(2,floor(log(n,2)+1))-2
	print(F(n,nl,nr,ql-1,qr-1,debug))

main(debug=False)