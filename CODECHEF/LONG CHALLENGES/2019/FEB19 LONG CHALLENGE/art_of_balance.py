def trythis(groupsize,occurnces,freq,occurnces_arr_size):
	operations=0
	for i in range(occurnces_arr_size):
		operations+=abs(occurnces[i]-groupsize)


	return operations//2

def balance(occurnces,slen):

	'''
	if slen in [3,5,7,11,13,17]:
		max_occurnce=max(occurnces)
		index_mo=occurnces.index(max_occurnce)
		operations=0
		balanced=True

		#divisible by 1
		for i in range(26):
			if occurnces[i]!=max_occurnce and occurnces[i]!=0:
				balanced=False
		if balanced:
			return 0

		#Divisible by itself
		for i in range(26):
			if i!=index_mo:
				operations+=occurnces[i]
		return operations

	'''
	if slen in [1,2] :
		return 0;

	else :
		max_occurnce=max(occurnces)
		index_mo=occurnces.index(max_occurnce)
		balanced=True
		for i in range(26):
			if occurnces[i]!=max_occurnce and occurnces[i]!=0:
				balanced=False
		if balanced:
			return 0

		
		freq=[0 for i in range(27)]
		pcnt=0
		for i in occurnces:
			if i!=0:
				freq[i]+=1
				pcnt+=1

		#print(occurnces,freq,sep="\n")
		
		mod=freq.index(max(freq))
		
		

		dividends=[]
		for i in range(1,slen//2 +1):
			if slen%i==0 :
				dividends.append(i)

		#print(dividends)
		
		minimum=99999999

		sorted_occurnces=sorted(occurnces,reverse=True)
		x=0
		for i in range(len(dividends)):
			if dividends[i]>mod:
				x=dividends[i]
				break





		temp=trythis(x,sorted_occurnces,freq,pcnt)
		#print(temp)
		if temp<minimum:
			minimum=temp
		return minimum


while True :
	try :
		for _ in range(int(input())):
			s=input().strip()
			length=len(s)
			cnt=[0 for i in range(26)]
			for l in s:
				cnt[ord(l)-65]+=1
		
			operations=balance(cnt,length)
			print(operations)		

	except:
		break