size = int(input())
string = input().strip()
queriesize = int(input())
queries=[]
for i in range(queriesize):
	queries.append(int(input()))
maxi = max(queries)
alpha = {chr(j):[] for j in range(97,123)}
#occurnces = [{ord(j):0 for j in range(97,123)} for i in range(size)]

#occurnces[0][string[0]]+=1
for i in range(size):
	#occurnces[i][string[i]]+=1
	#prev = occurnces[i-1][string[i]]
	#occurnces[i][string[i]]
	alpha[string[i]].append(i+1)

for index in queries:
	char = string[index-1]
	key= index-1
	ls=alpha[char]
	count=0
	'''
	for i in ls:
		if i>key:
			break
		count+=1
	'''
	print(count)