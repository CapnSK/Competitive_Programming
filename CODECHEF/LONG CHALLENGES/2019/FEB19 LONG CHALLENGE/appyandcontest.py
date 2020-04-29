def gcd(a,b):
	if a==0 and b==0 :
		return 0
	if a==0:
		return b
	elif b==0:
		return a
	else:
		return gcd(b,a%b)

def lcm(a,b):
	g=gcd(a,b)
	if g!=0:
		temp=a*b//g
		return temp
	return 0

while True:
	try :
		for _ in range(int(input())):
			n,a,b,k=map(int,input().split())
			ans = (n/a)+(n/b)-2*((n//lcm(a,b)))
			if ans >=k :
				print("Win")
			else :
				print("Lose")
	except : 
		break