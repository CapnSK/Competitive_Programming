BASE={str(i):i+1 for i in range(1,10)}
for i in range(65,91):
	BASE[chr(i)]=i-54

while True:
	try:
		for _ in range(int(input())):
			dp={}
			n=int(input())
			bases = [0 for i in range(n)]
			nums = ['0' for i in range(n)]
			knownBases=[]
			minBase=[2 for i in range(n)]
			for i in range(n):
				base,no = input().split()
				bases[i]=int(base)
				nums[i]=no
				if base != '-1':
					knownBases.append(i)
				if max(no) in BASE:
					minBase[i]=BASE[max(no)]
			for k in range(n):
				base = bases[k]
				if base==-1:
					unique=set()
					for j in range(minBase[k],37):
						no = int(nums[k],j)
						#print(no,end=' ')
						unique.add(no)
					for no in unique:
						if no in dp:
							dp[no]+=1
						else:
							dp[no]=1
				else:
					no = int(nums[k],base)
					if no in dp:
						dp[no]+=1
					else:
						dp[no]=1
			output=-1
			s= sorted(list(dp.items()),key=lambda x:x[0])
			for k,v in s:
				if v==n:
					output=k
					break
			if output <= (10**12):
				print(output)
			else:
				print(-1)
	except (ValueError,EOFError) as e:
		break