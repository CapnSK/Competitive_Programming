def isleap(year):
	if year%4 ==0 :
		if year%100 == 0 and year%400 == 0:
			return True
		if year%100 !=0:
			return True
	return False

days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

while True:
	try:
		for _ in range(int(input())):
			#print(isleap(int(input())))
			year = int(input())
			odd=0
			if year == 2001:
				print("monday")
			elif year<2001:
				temp = 2000
				odd = 0
				while(temp>=year):
					if(isleap(temp)):
						odd+=2
					else:
						odd+=1
					temp-=1
				odd = odd%7
				print(days[(7-odd)%7])
			elif year>2001:
				temp=2001
				odd=0
				while(temp<year):
					if(isleap(temp)):
						odd+=2
					else:
						odd+=1
					temp+=1
				odd = odd%7
				print(days[odd])


	except :
		break