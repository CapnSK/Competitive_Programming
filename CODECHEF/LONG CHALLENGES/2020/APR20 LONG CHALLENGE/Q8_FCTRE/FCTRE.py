spf=[-1 for i in range(1000001)]
spf[1]=1
def precompute():
	global spf
	for i in range(2,1000001,2):
		spf[i]=2
	for i in range(3,1000001,2):
		if spf[i]==-1:
			spf[i]=i
			for j in range(i*i,1000001,i):
				if spf[j]==-1:
					spf[j]=i


def getallpfs(n):
	global spf
	d={}
	while n>1:
		if spf[n] not in d:
			d[spf[n]]=0
		d[spf[n]]+=1
		n= n//spf[n]
	return d



def DFS(vis, x, y,E,stack,debug):
    stack.append(x)
    if debug:
    	print("Current node is",x)
    	print("Stack before",stack)
    if (x == y):
        #printPath(stack) 
        return [True,stack]
    vis[x] = True
    found=False
    flag = 0
    if (len(E[x]) > 0): 
        for j in E[x]: 
              

            if (vis[j] == False): 
                found,path=DFS(vis, j, y,E,stack,debug) 
                if found:
                    stack=path
                    flag = 1
                    break
  
    if (flag == 0):
        del stack[-1]
    if debug:
    	print("stack after",stack)
    return [found,stack]


def getPath(u,v,V,E,debug):
	visited=[False for i in range(V+1)]
	s=[]
	found,path=DFS(visited,u,v,E,s,debug)
	if debug:
		print("Final Path is",path)
	return path


def main(debug=False):
	precompute()
	MOD=1000000007
	for _ in range(int(input())):
		n=int(input())
		edges=[[] for i in range(n+1)]
		connected={}
		for i in range(n-1):
			u,v=map(int,input().split())
			u,v=min(u,v),max(u,v)
			edges[u].append(v)
			edges[v].append(u)
			connected[(u,v)]=True
		cost=list(map(int,input().split()))
		spfOfCosts=[]
		for i in cost:
			spfOfCosts.append(getallpfs(i))

		if debug:
			print("edges",edges)
			print("spfOfCosts",spfOfCosts)

		q=int(input())
		dp={}
		while q>0:
			q-=1
			u,v=map(int,input().split())
			u,v=min(u,v),max(u,v)
			ans=1
			if (u,v) not in dp:
				if u==v:
					ans=1
					for i in spfOfCosts[u-1].values():
						ans=(ans*(i+1)%MOD)%MOD
					print(ans%MOD)

				elif (u,v) in connected:
					upf=spfOfCosts[u-1]
					vpf=spfOfCosts[v-1]
					tmp={}
					for pf in upf:
						if pf not in tmp:
							tmp[pf]=0
						tmp[pf]+=upf[pf]

					for pf in vpf:
						if pf not in tmp:
							tmp[pf]=0
						tmp[pf]+=vpf[pf]

					ans=1
					for i in tmp.values():
						ans=(ans*((i+1)%MOD))%MOD
					print(ans%MOD)

				else:
					path=getPath(u,v,n,edges,debug)
					tmp={}
					if debug:
						print("Calculating final pfs")
					for node in path:
						if debug:
							print("curr node",node,"with value",cost[node-1],"has pfs",spfOfCosts[node-1])
						for pf in spfOfCosts[node-1]:
							if pf not in tmp:
								tmp[pf]=0
							tmp[pf]+=spfOfCosts[node-1][pf]
						if debug:
							print("Final pfs till",node,"with value",cost[node-1],"are",tmp)
					if debug:
						print("final pfs",tmp)
					ans=1
					for i in tmp.values():
						ans=(ans*((i+1)%MOD))%MOD
					print(ans%MOD)
				dp[(u,v)]=ans
			else:
				print(dp[(u,v)])




while True:
	try:
		main(debug=False)
	except (ValueError,EOFError) as e:
		break