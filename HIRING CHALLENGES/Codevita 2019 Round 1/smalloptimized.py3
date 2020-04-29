n=input()
a=list(map(int,input().split()))
d={}
for i in a:
	if i not in d:
		d[i]=1
	else:
		d[i]+=1
          
d=sorted(d.items(),key=lambda x : x[1])
print(d[-1][1])