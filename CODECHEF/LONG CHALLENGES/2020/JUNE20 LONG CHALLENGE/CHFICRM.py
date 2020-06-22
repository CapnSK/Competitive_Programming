def main(debug=False):
	for _ in range(int(input())):
		n=int(input())
		arr=list(map(int,input().split()))
		possible=True
		currency={5:0,10:0,15:0}
		for i in range(n):
			money=arr[i]
			if money>5:
				changeToGive = money - 5
				if changeToGive==5:
					if currency[5]<1:
						possible=False
						break
					currency[5]-=1
				elif changeToGive==10:
					if currency[5]<2 and currency[10]<1:
						possible=False
						break
					else:
						if currency[10]>=1:
							currency[10]-=1
						else:
							currency[5]-=2
						
			currency[money]+=1
		print("YES" if possible else "NO")
while True:
	try:
		main(debug=True)
	except (ValueError,EOFError) as e:
		break