from bisect import bisect_left,bisect_right
from functools import reduce

def ilen(iterable):
    return reduce(lambda sum, element: sum + 1, iterable, 0)

while True:
	try:
		for _ in range(int(input())):
			n=int(input())
			a = list(map(int,input().split()))

			processed=[]
			plen=0
			mv=0
			for i in a:
				ind = bisect_left(processed,i)
				processed.insert(ind,i)
				plen+=1
				sv=0
				#tmp=filter(lambda x:x%i==0,processed)
				tmp = [1 for k in processed if k%i==0]
				sv = len(tmp)
				# for j in range(ind+1,plen):
				# 	if processed[j]%i==0:
				# 		sv+=1
				if (sv-1)>mv:
					mv=sv-1

			print(mv)

	except (ValueError,EOFError) as e:
		break