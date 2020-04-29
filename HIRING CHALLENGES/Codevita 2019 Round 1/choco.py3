# fracts = {}

def cal(i,j):
	if i==j:
		return 1
	else:
		a=max(i,j)
		b=min(i,j)
		cnt=0
		# tempk = (str(a)+'/'+str(b))
		# if(tempk in fracts.keys()):
		# 		cnt+=fracts[tempk]
		# 		return cnt
		cn = 1
		while cn>0:
			# tempk = (str(a)+'/'+str(b))
			# if(tempk in fracts.keys()):
			# 	cnt+=fracts[tempk]
			# 	break
			# if a%b==0:
			# 	if((str(a)+'/'+str(b)) not in fracts.keys()):
			# 		fracts[tempk] = a//b
			# 	cnt+=a//b
			# 	break
			# cnt+=a//b
			# a,b=b,a%b
			# cn-=1
			cnt+=1
			cn -= 1
		return cnt

n=int(input())
m=int(input())
p=int(input())
q=int(input())

ans=0;
for j in range(p,q+1):
	if(j==1):
		ans += (n*(n+1)/2)-(m*(m-1)/2)
	else:
		if((m/j)==(n/j)):
			ans += (a[n%j][j]+(n-m+1)*(m/j))
			if((m%j)>0):
				ans -= a[(m%j)-1][j]
		else:
			ans += (a[j-1][j]+(j-(m%j))*(m/j)+a[n%j][j]+((n%j)+1)*(n/j))
			if((m%j)>0):
				ans -= a[(m%j)-1][j]
			if(((n/j)-(m/j)) > 1):
				ans += a[j-1][j]*((n/j)-(m/j)-1)
				ans += j*(((n/j)*((n/j)-1)/2)-((m/j)*((m/j)+1)/2))
	
print(ans)