while True:
	try:
		for _ in range(int(input())):
			n=int(input())
			scoreA,scoreB = 0,0
			for x in range(n):
				possible = False
				code,a,b = map(int,input().split())
				if code == 1 or a==b:
					scoreA = a
					scoreB = b
					possible = True
				else:
					a,b = min(a,b),max(a,b)

					if scoreA>scoreB:
						if scoreA>a and scoreB<=a:
							scoreA=b
							scoreB=a
							possible=True
						 
					elif scoreB>scoreA:
						if scoreB>a and scoreA<=a:
							scoreB=b
							scoreA=a
							possible=True

					else:
						possible = False

				print("YES" if possible else "NO")


	except:
		break