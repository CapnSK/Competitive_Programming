# size = int(input())
# string = input().strip()
# queriesize = int(input())
# queries=[]
# for i in range(queriesize):
# 	queries.append(int(input()))
# maxi = max(queries)
# occurnces = [{chr(j):0 for j in range(97,123)} for i in range(size)]

# occurnces[0][string[0]]+=1
# #print(occurnces[0])
# for i in range(1,size):
# 	# occurnces[i][string[i]]+=1
# 	# prev = occurnces[i-1][string[i]]
# 	# occurnces[i][string[i]]
# 	occurnces[i].update(occurnces[i-1])
# 	occurnces[i][string[i]]+=1
# 	#print(occurnces[i])

# for index in queries:
# 	char = string[index-1]
# 	key= index-1
# 	print(occurnces[key-1][char])
size = int(input())
string = input().strip()
queriesize = int(input())
queries=[]
for i in range(queriesize):
	queries.append(int(input()))
maxi = max(queries)
occurnces = [{} for i in range(size)]

occurnces[0][string[0]]=1
#print(occurnces[0])
for i in range(1,size):
	# occurnces[i][string[i]]+=1
	# prev = occurnces[i-1][string[i]]
	# occurnces[i][string[i]]
	#occurnces[i].update(occurnces[i-1])
	prev = occurnces[i-1]
	for key,value in prev.items():
		occurnces[i][key]=value
	if string[i] in occurnces[i]:
		occurnces[i][string[i]]+=1
	else:
		occurnces[i][string[i]]=1
	#print(occurnces[i])

for index in queries:
	char = string[index-1]
	key= index-1
	print(occurnces[key-1][char] if char in occurnces[key-1] else 0)