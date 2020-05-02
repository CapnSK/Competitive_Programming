from math import floor,sqrt
def possible(minutes,cooks,n,pr,debug):
	countPr=0
	if debug:
		print("cooks",cooks)
	for i in range(n):
		r=cooks[i]
		countPr+= floor((-1+sqrt(1+4*((2*minutes)/r))))//2
		if debug:
			print("parathas after ",i,"cook",countPr)
		if countPr>=pr:
			return True
	return False

def getAns(pr,cooks,n,debug):
	s = 1
	e = cooks[0]*((pr*(pr+1))//2) 
	ans=-1
	while s<=e:
		mid = (s+e)//2
		if debug:
			print("befor\ns,e,mid",s,e,mid)
		poss = possible(mid,cooks,n,pr,debug)
		if debug:
			print("possible for mid:",mid,poss)
		if poss:
			e=mid-1
			ans=mid
		else:
			s=mid+1
		if debug:
			print("after\ns,e,mid",s,e,mid)
	return ans
def main(debug=False):
	for _ in range(int(input())):
		pr=int(input())
		cooks=list(map(int,input().split()))
		n=cooks[0]
		cooks=cooks[1::]
		if debug:
			print("pr,n,cooks",pr,n,cooks)
		print(getAns(pr,cooks,n,debug))

main(debug=False)