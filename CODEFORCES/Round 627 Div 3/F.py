import sys
sys.setrecursionlimit(100000000)

def dfs1(node,parent=-1):
	global dp1,a,e,n,dp2
	dp1[node]=a[node]
	for ch in e[node]:
		if ch==parent:
			continue
		dfs1(ch,node)
		dp1[node]+=max(0,dp1[ch])


def dfs2(node,parent=-1):
	global dp1,a,e,n,dp2
	dp2[node]=dp1[node]
	if parent!=-1:
		val = dp2[parent]-max(0,dp1[node])
		dp2[node] += max(0,val)
	for ch in e[node]:
		if ch==parent:
			continue
		dfs2(ch,node)

debug = False
n=int(input())
dp1=[0]*(n+1)
dp2=[0]*(n+1)
a=[0]+list(map(int,input().split()))
for i in range(n+1):
	if a[i]==0 and i!=0:
		a[i]=-1
if debug:
	print("a",a[1::])
e=[[] for i in range(n+1)]
for i in range(n-1):
	u,v=map(int,input().split())
	e[u].append(v)
	e[v].append(u)

dfs1(1)
dfs2(1)

print(*dp2[1::])