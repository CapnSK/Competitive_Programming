while True :
	try :
		for _ in range(int(input())):
			n=int(input())
			s=input()
			possible_passwords={}
			for i in range(1,n+1):
				temp=s[:i]
				if i>n//2:
					possible_passwords[temp]=1
				else:
					cnt=s.count(temp)
					possible_passwords[temp]=cnt

			#print(possible_passwords)

			max_occured=-99999
			prev_len=0
			password="no"
			for possible in possible_passwords :
				
				poss_len=len(possible)
				if max_occured<possible_passwords[possible] and poss_len>prev_len:
					max_occured=possible_passwords[possible]
					prev_len=poss_len
					password=possible

			print(password)
			
	except :
		break