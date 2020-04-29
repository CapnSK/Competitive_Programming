def main(debug=False):
	for _ in range(int(input())):
		n=int(input())
		a=list(map(int,input().split()))
		b=list(map(int,input().split()))
		a.sort()
		b.sort()
		sum=0
		for i in range(n):
			sum+=min(a[i],b[i])
		print(sum)

while True:
	try:
		main(debug=False)
	except (EOFError,ValueError) as e:
		break