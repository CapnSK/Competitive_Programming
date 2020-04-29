def main(debug=False):
	for _ in range(int(input())):
		n,k=map(int,input().split())
		a=list(map(int,input().split()))
		sum=0
		for i in range(n):
			sum+=(a[i]%k)
		print(sum%k)
		
while True:
	try:
		main(debug=False)
	except (EOFError,ValueError) as e:
		break