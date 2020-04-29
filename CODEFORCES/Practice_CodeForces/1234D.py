from bisect import bisect_left

s=input().strip()
s=[c for c in s]
q=int(input())

occ={}

for i,c in enumerate(s):
	if c in occ:
		occ[c].append(i+1)
	else:
		occ[c]=[]
		occ[c].append(i+1)

for t in range(q):
	tmp=input().strip().split()
	if tmp[0]=='1':
		ind,charToReplace = int(tmp[1]),tmp[2]
		oldchr=s[ind-1]
		occ[oldchr].remove(ind)
		insertindex = bisect_left(occ[charToReplace],ind)
		occ[charToReplace].insert(insertindex,ind)
		s[ind-1]=charToReplace
		#print(occ.items())
	elif tmp[0]=='2':
		l,r = int(tmp[1]),int(tmp[2])
		cnt=0
		for key in occ.keys():
			indices = occ[key]
			#print("indices",indices)
			left=bisect_left(indices,l+1)
			right=bisect_left(indices,r+1)
			if right-left>=1:
				cnt+=1
			#print("r l c",right,left)
		print(cnt)