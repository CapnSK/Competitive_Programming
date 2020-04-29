def main(debug=False):
	MOD=1000000007
	for _ in range(int(input())):
		n=int(input())
		a=list(map(int,input().split()))
		a.sort(reverse=True)
		yearsPassed=0
		profit=0
		for price in a:
			profit=(profit+ max(0,price-yearsPassed)%MOD)%MOD
			if price==0:
				break
			yearsPassed+=1
		print(profit%MOD)


while True:
	try:
		main(debug=False)
	except (ValueError,EOFError) as e:
		break