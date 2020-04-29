n=int(input())
arr=[]
ans=[]
mul=1
for i in range(n):
	cur = int(input())
	arr.append(cur)
	mul*=cur

for i in arr:
	ans.append(mul//i)

return ans