def main(debug=False):
	for _ in range(int(input())):
		n=int(input())
		l,r=[],[]
		for i in range(n):
			lr=list(map(int,input().split()))
			l.append(lr[0])
			r.append(lr[1])

		l.sort()
		r.sort()

		if debug:
			print(l)
			print(r)
		lp,rp,mp=0,0,0
		merged=[0 for i in range(2*n)]
		if debug:
			print(merged)
		cnt=0
		while True:
			if mp==2*n:
				break
			if lp==n:
				merged[mp::]=[cnt-(i-rp+1) for i in range(rp,n)]
				break
			if rp==n:
				merged[mp::]=[cnt+(i-lp+1) for i in range(lp,n)]
				break
			if debug:
				print("For i=",mp,"l[lp] r[rp]",l[lp],r[rp])
			if l[lp]<r[rp]:
				cnt+=1
				merged[mp]=cnt
				lp+=1
			elif l[lp]==r[rp]:
				cnt+=1
				merged[mp]=cnt
				lp+=1
			elif l[lp]>r[rp]:
				cnt-=1
				merged[mp]=cnt
				rp+=1
			mp+=1

		if debug:
			print(merged)

		prev=merged[0]
		flag=False
		count=((10**5) +1)
		for i in range(1,2*n -1):
			curr=merged[i]
			if curr>prev:   # denotes arrival
				if flag:
					count=min(count,merged[i]-1)
			elif curr<prev: # denotes departure
				flag=True
			prev=curr
		if debug:
			print("Count",count)
		if count==((10**5) +1):
			print(-1)
		else:
			print(count)


main(debug=False)