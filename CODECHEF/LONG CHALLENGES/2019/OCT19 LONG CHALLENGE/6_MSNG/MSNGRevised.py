BASE={str(i):i+1 for i in range(1,10)}
for i in range(65,91):
	BASE[chr(i)]=i-54
print(BASE)
while True:
	try:
		for _ in range(int(input())):
			n=int(input())
			bases = [0 for i in range(n)]
			nums = ['0' for i in range(n)]
			knownBases=[]

			for i in range(n):
				base,no = input().split()
				bases[i]=int(base)
				nums[i]=no
				if base != '-1':
					knownBases.append(i)

			X=-1
			print(bases)
			print(nums)
			if len(knownBases)>0:
				tempVal = int(nums[knownBases[0]],bases[knownBases[0]])
				possible=True
				if len(knownBases)>1:
					for i in range(1,len(knownBases)):
						b = knownBases[i]
						currBase = bases[b]
						currNum = nums[b]

						currDecimalEq = int(currNum,currBase)
						if currDecimalEq!= tempVal:
							possible=False
							break
				if possible:
					X=tempVal
					unknownBaseCount = n-len(knownBases)
					for i in range(n):
						base =bases[i]
						if base==-1:
							no = nums[i]
							minBase = BASE[max(no)]
							#print(minBase)
							base = minBase
							while True:
								if base>36:
									break
								currDecimalEq = int(no,base)
								if currDecimalEq==X:
									unknownBaseCount-=1
									break
								base+=1

					if unknownBaseCount>0:
						X=-1
			else :
				pass


			print(X if X<=pow(10,12) else -1)

	except (ValueError,EOFError) as e:
		break