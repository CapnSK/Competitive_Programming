BASE = {'1':2,'2':3,'3':4,'4':5,'5':6,'6':7,'7':8,'8':9,'9':10}
for i in range(65,91):
	BASE[chr(i)]=i-54

#print(BASE)
while True:
	try:
		for _ in range(int(input())):
			n=int(input())
			bases = []
			nums = []
			knownbases=[]
			minBase=[]
			minValue=[]

			for i in range(n):
				b,n1 = input().strip().split()
				bases.append(int(b))
				if b!='-1':
					knownbases.append(i)
				nums.append(n1)
				minBase.append(BASE[max(n1)])
				
				minValue.append(int(n1,minBase[-1]))
				
			#print(len(knownbases))
			if len(knownbases)>0:
				firstVal=-1
				possible=True
				for i in knownbases:
					if firstVal==-1:
						firstVal=int(nums[i],bases[i])

					currval=int(nums[i],bases[i])
					if currval!=firstVal:
						possible=False
						break
				if possible:
					#print(minBase)
					#print(minValue)
					if max(minValue)>firstVal:
						#print("YAHA")
						print(-1)
						continue
					else:
						ok=True
						for i in range(n):
							if bases[i]==-1:
								#print(nums[i])
								sv=minValue[i]
								sb=minBase[i]
								for j in range(sb,37):
									tmp = int(nums[i],j)
									#print(j,tmp,firstVal)
									if tmp>firstVal:
										ok=False
										break
									elif tmp==firstVal:
										break
										ok=True
									else:
										continue
							if not ok:
								#print("not ok")
								break
						if ok:
							print(firstVal)
							continue


				else:
					#print("WAHA")
					print(-1)
					continue
			else:
				print(-1)
				continue
				#print(knownbases,possible,firstVal)





	except (ValueError,EOFError) as e:
		break