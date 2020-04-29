while True:
	try:
		for _ in range(int(input())):
			nchr,d=input().split()
			n=len(nchr)
			nchr=list(nchr)
			d=int(d)
			arranged=[]
			for i in range(n):
				arranged.append([nchr[i],i])
			arranged=sorted(arranged,key=lambda x:x[0])
			#print(arranged)

			last_index=-99999
			smallest=[]

			for number,index in arranged:
				number=int(number)
				if last_index<index :
					if number<d:
						smallest.append(str(number))
					elif number>d :
						smallest.append(str(d))
					last_index=index
				else:
					continue
			
			repeat=n-len(smallest)

			for i in range(repeat):
				smallest.append(str(d))

			print(''.join(smallest))
			


	except:
		break