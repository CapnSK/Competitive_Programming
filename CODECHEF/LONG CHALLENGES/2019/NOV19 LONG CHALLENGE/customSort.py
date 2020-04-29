# def comp(p1,p2):
# 	if p1[0]>p2[0]:
# 		return 1
# 	elif p1[0]<p2[0]:
# 		return -1
# 	elif p1[0]==p2[0]:
# 		if p1[1]>p2[1]:
# 			return 1
# 		else:
# 			return -1
from bisect import bisect_left,bisect_right
def lexSort(arr):
	arr=sorted(arr,key=lambda x:x[0])
	d={}
	for k,v in arr:
		if k in d:
			d[k].insert(bisect_left(d[k],v),v)
		else:
			d[k]=[v]
	newArr=[]
	for k in d:
		temp=d[k]
		for v in temp:
			newArr.append([k,v])
	return newArr


arr=[list(map(int,input().split())) for i in range(int(input()))]
print(lexSort(arr))