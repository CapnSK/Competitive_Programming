from collections import OrderedDict
n,k = map(int,input().split())
convs = list(map(int,input().split()))
x=[]
window=OrderedDict()
chats=0
for curr_conv in convs:
	if curr_conv not in window:
		window[curr_conv]=0

	if window[curr_conv]==0:
		if chats<=k-1:
			x.append(curr_conv)
			window[curr_conv]+=1
			chats+=1

		if chats==k:
			window[x[0]]-=1
			del x[0]
			x.append(curr_conv)
			window[curr_conv]+=1

print(len(x))
print(*x[::-1])