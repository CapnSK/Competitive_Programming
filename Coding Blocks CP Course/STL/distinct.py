def main(debug=False):
	n=int(input())
	a=list(map(int,input().split()))
	ans=0
	for i in range(n):
		curr=a[i]
		ans+=1
		j=i+1
		d={curr:1}
		if debug:
			print("for curr",curr,"d is",d)
		while True:
			if j>=n:
				#ans+=(j-1-i)
				break
			if debug:
				print("j is",j,"a[j]",a[j])
			if a[j] in d:
				if debug:
					print(a[j],"is present in d",d,"ans is",ans)
				break
			else:
				d[a[j]]=1
			ans+=(j-i)+1
			if debug:
				print("for",j,"ans is",ans)

			j+=1
		if debug:
			print("ans after",i,a[i],ans)
	print(ans)
main(debug=False)