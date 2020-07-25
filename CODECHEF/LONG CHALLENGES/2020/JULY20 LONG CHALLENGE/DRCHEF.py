def main(debug=False):
	for _ in range(int(input())):
		n,x = map(int,input().split())
		arr = list(map(int,input().split()))
		arr.sort()
		days=0
		for i in arr:
			if x>=i:
				days+=1
				x=max(x,i*2)
			else:
				while x<i:
					x=x<<1
					days+=1
				days+=1
				x=i<<1
		print(days)

while True:
	try:
		main(debug=False)
	except (ValueError,EOFError) as e:
		break