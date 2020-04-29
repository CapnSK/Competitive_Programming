for _ in range(int(input())):
	n=int(input())
	moves=[]
	for i in range(n):
		temp=input().strip()
		moves.append([temp,len(temp)])
	#print(moves)
	Mybot=[]
	impossible=False
	Won = False
	alreadyWon=[False for i in range(n)]
	for i in range(500):
		R,S,P=False,False,False
		for j in range(n):
			if not alreadyWon[j]:
				Lj=moves[j][1]
				index=i%Lj
				if moves[j][0][index] == 'R' :
					R=True
				elif moves[j][0][index] == 'S' :
					S=True
				elif moves[j][0][index] == 'P' :
					P=True


		if R and S and P:
			impossible=True
			break


		if R and S and not P:
			Mybot.append('R')
			for j in range(n):
				Lj=moves[j][1]
				index=i%Lj
				if moves[j][0][index]=='S':
					alreadyWon[j]=True

		if R and P and not S:
			Mybot.append('P')
			for j in range(n):
				Lj=moves[j][1]
				index=i%Lj
				if moves[j][0][index]=='R':
					alreadyWon[j]=True

		if P and S and not R:
			Mybot.append('S')
			for j in range(n):
				Lj=moves[j][1]
				index=i%Lj
				if moves[j][0][index]=='P':
					alreadyWon[j]=True



		if R and not P and not S:
			Mybot.append('P')
			Won=True
			break
		if S and not R and not P:
			Mybot.append('R')
			Won=True
			break
		if P and not S and not R:
			Mybot.append('S')
			Won=True
			break

	if i==499 and not Won:
		impossible=True

	print("Case #",_+1,":",sep="",end=" ")
	if impossible:
		print("IMPOSSIBLE")
	elif Won :
		print(''.join(Mybot))