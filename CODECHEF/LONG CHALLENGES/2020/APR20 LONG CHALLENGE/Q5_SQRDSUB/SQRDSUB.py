from bisect import bisect_left
def get4Count(arr,n,debug=False):
	ans=0
	mods=[[],[],[],[]]
	for i in range(n):
		mods[arr[i]%4].append(i)

	for i in range(n):
		ind2=bisect_left(mods[2],i)
		ind4=bisect_left(mods[0],i)
		if debug:
			print(i,ind2,mods[2],ind4,mods[0])
		nextInd=-1
		if ind4<len(mods[0]):
			nextInd=mods[0][ind4]
		if ind2+1<len(mods[2]):
			if nextInd==-1:
				nextInd=mods[2][ind2+1]
			else:
				nextInd=min(nextInd,mods[2][ind2+1])
		if debug:
			print("nextInd",nextInd)
		if nextInd!=-1:
			ans+= (n-nextInd)
		if debug:
			print("ans for",i,"is",ans)
	return ans

def getOddCount(arr,n,debug=False):
	ans=0
	i=0
	while i<n:
		if arr[i]&1:
			start,end=i,i
			cnt=0
			while end<n and arr[end]&1:
				cnt+=1
				end+=1
			#print(i,cnt)
			ans+=((cnt)*(cnt+1))//2
			i=end
		else:
			i+=1
	if debug:
		print("final getOddCount",ans)
	return ans

def main(debug=False):
	#precompute()
	for _ in range(int(input())):
		n=int(input())
		arr=list(map(int,input().split()))
		k1=getOddCount(arr,n,debug)
		k2=get4Count(arr,n,debug)
		print(k1+k2)
while True:
	try:
		main(debug=False)
	except (ValueError,EOFError) as e:
		break