while True :
	try :
		for _ in range(int(input())):
			n=int(input())
			arr=list(map(int,input().split()))
			pcnt=0
			ncnt=0
			for i in arr :
				if i<0 :
					ncnt+=1
				else :
					pcnt+=1
			
			if ncnt>=pcnt and pcnt!=0:
				print(ncnt,pcnt)
			elif ncnt>pcnt and pcnt==0:
				print(ncnt,ncnt)
			elif pcnt>=ncnt and ncnt!=0:
				print(pcnt,ncnt)
			elif pcnt>ncnt and ncnt==0:
				print(pcnt,pcnt)


	except :
		break