arr=[4,8,15,16,23,42]
dist_prods={arr[i]*arr[j]: [arr[i],arr[j]] for i in range(len(arr)) for j in range(i+1,len(arr))}
visited={i:False for i in arr}
ouput=[]
prev=[]
for i in range(4):
	print('? {0} {1}'.format(i+1,i+2), flush=True)
	prod=int(input())
	if i==0:
		prev=dist_prods[prod]
	if i>=1:
		curr=dist_prods[prod]
		if prev[0]==curr[0] or prev[0]==curr[1]:
			if not visited[prev[1]]:
				ouput.append(prev[1])
			if not visited[prev[0]]:
				ouput.append(prev[0])
		elif prev[1]==curr[0] or prev[1]==curr[1]:
			if not visited[prev[0]]:
				ouput.append(prev[0])
			if not visited[prev[1]]:
				ouput.append(prev[1])

		visited[prev[0]]=True
		visited[prev[1]]=True
		if i==3:
			if not visited[curr[0]]:
				ouput.append(curr[0])
				visited[curr[0]]=True
			if not visited[curr[1]]:
				ouput.append(curr[1])
				visited[curr[1]]=True
		prev=curr
for k in visited:
	if visited[k]==False:
		ouput.append(k)
print('! {0} {1} {2} {3} {4} {5}'.format(*ouput))