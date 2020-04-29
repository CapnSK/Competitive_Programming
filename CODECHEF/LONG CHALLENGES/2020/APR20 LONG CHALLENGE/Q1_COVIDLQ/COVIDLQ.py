def main(debug=False):
	for _ in range(int(input())):
		n=int(input())
		arr=list(map(int,input().split()))
		lstInd=-1
		Violated=False
		for i in range(n):
			if arr[i]==1:
				if lstInd!=-1:
					if i-lstInd<6:
						Violated=True
						break
				lstInd=i

		print("YES" if not Violated else "NO")

while True:
	try:
		main(debug=False)
	except (ValueError,EOFError) as e:
		break