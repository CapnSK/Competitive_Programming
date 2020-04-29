start=int(input())
end =int(input())
c=0
for i in range(start,end+1):
	for j in range(i+1,end+1):
		print(i,j)
		c+=1
print(c)