def mult(M,m,ans=0):
	if m==0:
		return ans
	m-=1
	return mult(M,m,ans+M)

print(mult(5,3))