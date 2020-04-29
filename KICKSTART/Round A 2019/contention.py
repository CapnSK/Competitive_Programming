'''
def sorting(queries):
	temp1=queries
	diff=[]
	i=0
	for l,r in temp1:
		diff.append([r-l,i])
		i+=1
'''



for _ in range(int(input())):
	n,q=map(int,input().split())
	queries=[]
	for x in range(q):
		queries.append(list(map(int,input().split())))

	#q1=sorting(queries)   #,key=lambda x:(x[1]-x[0]))
	q1=sorted(queries,key= lambda x:(x[1]-x[0]))
	#print(q1)
	