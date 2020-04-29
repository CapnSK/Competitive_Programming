while True :
		try :
			for _ in range(int(input())):
				n,b=map(int,input().split())
				options=[]
				for i in range(n):
					w,h,c=map(int,input().split())
					options.append([c,w*h])
				#print(*options)

				options=sorted(options)

				maximum=-99999

				for specs in options:
					if specs[0]<=b and specs[1]>maximum:
						maximum=specs[1]
					if specs[0]>b :
						break

				print(maximum if maximum>=0 else "no tablet")

		except :
			break