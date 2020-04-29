import math

while True:
	try :
		for _ in range(int(input())):
			n,k=map(int,input().split())
			queue=list(map(int,input().split()))
			max_pos=n+1
			angers=[]
			for i in range(n-1,-1,-1):
				sum1=0
				l=1
				for j in range(i,n):
					sum1+=int(math.floor(queue[j]/l))
					l+=1
				if sum1<= k:
					angers.append([i+1,sum1])



				'''
				if sum1<=k:
					#print(sum1,max_pos)
					max_pos=i+1
				elif sum1>k:
					break
				'''

			print(sorted(angers,key=lambda x:x[0])[0][0])

	except :
		break