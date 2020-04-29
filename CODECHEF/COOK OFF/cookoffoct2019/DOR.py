while True:
	try:
		for _ in range(int(input())):
			l,r = map(int,input().split())
			l,r=min(l,r),max(l,r)
			binL= bin(l)[2::]
			binR= bin(r)[2::]
			llen=len(binL)
			rlen=len(binR)
			binL='0'*(rlen-llen)+binL
			llen=rlen
			ans=[]
			ind=-1
			i=0
			while i<rlen and binR[i]==binL[i]:
				ans.append(binR[i])
				ind=i
				i+=1
			ans+=['1']*(rlen-1-ind)
			print(int(''.join(ans),2))


	except (ValueError,EOFError) as e:
		break