def query(ST,qs,qe,ss,se,nodeInd,debug):
	if qs>se or qe<ss:
		return float('inf')
	if qs<=ss and se<=qe:
		return ST[nodeInd]
	mid = (ss+se)//2
	l = query(ST,qs,qe,ss,mid,2*nodeInd+1,debug)
	r = query(ST,qs,qe,mid+1,se,2*nodeInd+2,debug)
	return min(l,r)

def update(ST,arrInd,val,ss,se,nodeInd,debug):
	if arrInd>se or arrInd<ss:
		return
	if ss==se and ss==arrInd:
		ST[nodeInd] = val
		return
	mid = (ss+se)//2
	update(ST,arrInd,val,ss,mid,2*nodeInd+1,debug)
	update(ST,arrInd,val,mid+1,se,2*nodeInd+2,debug)
	ST[nodeInd] = min(ST[2*nodeInd+1],ST[2*nodeInd+2])
	return


debug=False
n = int(input())
cities = list(map(int,input().split()))
k = int(input())

if cities[-1] == -1:
	print(-1)
else:
	dp = [float('inf') for i in range(n)]
	ST = [float('inf') for i in range(4*n +1)]
	dp[0] = cities[0]
	update(ST,0,cities[0],0,n-1,0,debug)
	for i in range(1,n):
		if cities[i]==-1:
			continue
		qs = max(i-k-1,0)
		qe = i-1
		prev = query(ST,qs,qe,0,n-1,0,debug)
		if debug:
			print(i,qs,qe,prev)
		val = prev + cities[i]
		update(ST,i,val,0,n-1,0,debug)
		dp[i] = val
	print(dp[n-1])


# for j in range(k+1):
		# 	if i-j<0:
		# 		break
		# 	prev = i-j-1
		# 	if cities[prev]!=-1:
		# 		dp[i] = min(dp[prev]+cities[i],dp[i])
		#print(dp)