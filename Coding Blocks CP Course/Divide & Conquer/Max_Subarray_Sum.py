def DnC(arr,s,e,debug):
	if s==e:
		return arr[s]
	mid=(s+e)//2
	pre=-1000000000000
	Sum=0
	for i in range(mid,s-1,-1):
		Sum+=arr[i]
		if debug:
			print("Sum for suff after",i,Sum)
		if Sum>pre:
			pre=Sum
	suff=-1000000000000
	Sum=0
	for i in range(mid+1,e+1):
		Sum+=arr[i]
		if debug:
			print("Sum for pre after",i,Sum)
		if Sum>suff:
			suff=Sum
	if debug:
		print(suff,pre)
	return max(suff+pre,DnC(arr,s,mid,debug),DnC(arr,mid+1,e,debug))

def getAns(arr,n,debug):
	s=0
	e=n-1
	return DnC(arr,s,e,debug)

def main(debug=False):
	for _ in range(int(input())):
		n=int(input())
		arr=list(map(int,input().split()))
		print(getAns(arr,n,debug))

main(debug=False)