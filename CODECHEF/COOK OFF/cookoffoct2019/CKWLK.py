from math import log2
while True:
	try:
		for _ in range(int(input())):
			n=input()
			nlen= len(n)
			no=0
			power=0
			ind=-1
			for i in range(nlen-1,-1,-1):
				if n[i]=='0':
					power+=1
				else:
					ind=i
					break
			#print(ind)
			if ind>=0:
				no=int(n[:ind+1:])
				p2 = log2(no)
				#print(no,p2)
				if int(p2)==p2:
					if power>=p2:
						print("Yes")
					else:
						print("No")
				else:
					print("No")
			else:
				if int(n)==1:
					print("Yes")
				else:
					print("No")

	except (ValueError,EOFError) as e:
		break