def main(debug=False):
	for _ in range(int(input())):
		n=int(input())
		W=[]
		for i in range(n-1):
			u,v,wi=map(int,input().split())
			W.append(wi)
		N=list(map(int,input().split()))
		N=sorted(N,reverse=True)
		W=sorted(W,reverse=True)
		W.insert(1,W[0])
		if debug:
			print("W",W)
			print("N",N)
		j=0
		cnt=0
		for i in W:
			if debug:
				print("for W[i]=",i,"and N[j]=",N[j])
			if i>N[j]:
				cnt+=1
			else:
				j+=1
			if debug:
				print("cnt for this iteration is",cnt)
		print(cnt)

main(debug=False)