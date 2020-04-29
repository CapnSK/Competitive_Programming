from math import sqrt
def getpfcount(n):
	count=0
	while n%2==0:
		count+=1
		n=n//2
	for i in range(3,int(sqrt(n))+1,2):
		while n%i==0:
			count+=1
			n=n//i
	if n>2:
		count+=1
	return count

def main(debug=False):
	t=int(input())
	for _ in range(t):
		x,k=map(int,input().split())
		Xpfs=getpfcount(x)
		if Xpfs>=k:
			print(1)
		else:
			print(0)

while True:
	try:
		main(debug=False)
	except (ValueError,EOFError) as e:
		break