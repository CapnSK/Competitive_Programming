for _ in range(int(input())) :
	n=int(input())
	lydia=input().strip()
	myPath=''
	for mov in lydia :
		if mov == 'S' :
			myPath+='E'
		elif mov == 'E' :
			myPath+='S'
	print("Case #",_+1,":",sep="",end=" ")
	print(myPath)