def main(debug=False):
	for _ in range(int(input())):
		n,k=map(int,input().split())
		p=list(map(int,input().split()))
		ans1,ans2=0,0
		for i in p:
			ans2+=i
			if i>k:
				ans1+=k
			else:
				ans1+=i
		print(ans2-ans1)
while True:
	try:
		main(debug=True)
	except (ValueError,EOFError) as e:
		break