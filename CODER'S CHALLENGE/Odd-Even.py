n = int(input())
lis = list(map(int,input().split()))
lis2 = [1 if i %2 == 0 else -1 for i in lis]
cnt = 0
for i in range(n):
	for j in range(i+1,n,2):
		if sum(lis2[i:j+1:1]) == 0:
			cnt +=1
print(cnt)