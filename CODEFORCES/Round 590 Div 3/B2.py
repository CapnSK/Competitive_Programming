n,k = map(int,input().split())
convs = list(map(int,input().split()))
x=[]
size=0
window={}
for conv in convs:
	if conv not in window or not window[conv]:
		window[conv]=True
		if size==k:
			window[x[0]]=False
			del x[0]
		elif size<k:
			size+=1
		x.append(conv)

print(size)
print(*x[::-1])