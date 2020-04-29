while True:
	try :
		for _ in range(int(input())):
			n=int(input())
			attack=list(map(int,input().split()))
			defense=list(map(int,input().split()))

			enemyattack=[]
			enemyattack.append(attack[-1]+attack[1])

			for i in range(n-2):
				enemyattack.append(attack[i]+attack[i+2])

			enemyattack.append(attack[-2]+attack[0])
			#print(enemyattack)

			possible= False
			max1=-99999
			for i in range(n):
				if(defense[i]>enemyattack[i] and defense[i]>max1):
					possible=True
					max1=defense[i]
			if not possible:
				print(-1)
			else:
				print(max1)

			
	except : 
		break