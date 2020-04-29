def isLeap(year):
	if year % 4 != 0:
		return False
	else:
		if year % 100 ==0 :
			if year %400 !=0:
				return False
			else:
				return True
		else:
			return True

# year=int(input())
# while(year>0):
# 	print(isLeap(year))
# 	year=int(input())

while True:
	try:
		months=[31,-1,31,30,31,30,31,31,30,31,30,31]



		for _ in range(int(input())):

			year,month,date=map(int,input().strip().split(':'))


			if isLeap(year):
				months[1]=29
			else:
				months[1]=28
			mismatched = False
			count=0
			initiallyOdd = True
			monthptr=month

			if date%2 == 0:
				initiallyOdd = False
			else:
				initiallyOdd = True

			while not mismatched:
				count+=1
				date+=2
				if date >= months[monthptr]:
					date=date%(months[monthptr])
					monthptr+=1
				if (date%2 == 0) != initiallyOdd:
					mismatched=True


	except (ValueError,EOFError):
		break
