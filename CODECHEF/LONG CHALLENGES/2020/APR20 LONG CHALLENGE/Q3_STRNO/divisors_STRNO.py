pfs=[-1 for i in range(500008)]
def precompute():
	global pfs
	pfs[2]=2
	pfs[1]=1
	for i in range(4,len(pfs),2):
		pfs[i]=2
	for i in range(3,len(pfs),2):
		if pfs[i]==-1:
			pfs[i]=i
			for j in range(i*i,len(pfs),i):
				if pfs[j]==-1:
					pfs[j]=i
def getpfcount(n):
	global pfs
	s=set()
	while n>1:
		s.add(pfs[n])
		n=n//pfs[n]
	return len(s)
from collections import defaultdict
precompute()
dp=dict()
def getDivs(n):
	i=1
	arr=[]
	while i*i <= n:
		if n%i==0:
			arr.append(i)#,end=" ")
			if i!=n//i:
				arr.append(n//i)#,end=" ")
		i+=1
	return arr
#print(getDivs(64*3*5))
for n in range(1,100000):
	arr=getDivs(n)
	l=len(arr)
	p=getpfcount(n)
	#print(len(arr),getpfcount(n))
	if p not in dp:
		dp[p]=dict()
	if l not in dp[p]:
		dp[p][l]=[]
	dp[p][l].append(n)
for k in dp:
	print(k,end=' :\n')
	for k1 in sorted(dp[k]):
		print('\t',k1,end=' : ')
		print(len(dp[k][k1]),dp[k][k1][0])
