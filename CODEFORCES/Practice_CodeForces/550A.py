s= input().strip()

acnt,bcnt=0,0
MaxA,MaxB,MinA,MinB = -1,-1,9999999999999,9999999999999

for i in range(len(s)-1):
	if s[i]=='A' and s[i+1]=='B':
		acnt+=1
		if i<MinA:
			MinA=i
		if i>MaxA:
			MaxA=i

	if s[i]=='B' and s[i+1]=='A':
		bcnt+=1
		if i<MinB:
			MinB=i
		if i>MaxB:
			MaxB=i
#print(acnt,cnt,MinA,MaxA,MinB,MaxB)
if (acnt>=1 and bcnt>=1) and (MaxB-MinA >1 or MaxA-MinB>1):
	print("YES")
else:
	print("NO")