from math import pow

denominator=[int(pow(2,i)) for i in range(1,30)]
numerator=[0 for i in range(1,30)]

numerator[0]=1
numerator[1]=1

for i in range(2,29):
	if i%2==0 :
		numerator[i]=numerator[i-1]*2 + 1
	else :
		numerator[i]=numerator[i-2]*4 + 1

t=list(map(int,input().split()))

for _ in range(1,t[0]+1):
	print(numerator[t[_]-1],denominator[t[_]-1],sep=" ",end=" ")