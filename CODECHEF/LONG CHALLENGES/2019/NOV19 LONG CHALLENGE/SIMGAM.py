def main(debug=False):
	for _ in range(int(input())):
		r=int(input())
		n=0
		arr=[]
		for i in range(r):
			t=list(map(int,input().split()))
			n+=t[0]
			arr.append(t)

		ans=0
		if n%2==1:
			n=(n//2)+1
		else:
			n=n//2
		if debug:
			print("n before",n)
			print("arr",arr)
		for i in range(r):
			colcnt=arr[i][0]
			ans+=sum(arr[i][1:(colcnt//2)+1:])
			if debug:
				print("ans for ",i,ans)
			n-=colcnt//2
			if debug:
				print("n for",i,n)
		if debug:
			print("n after",n)
		if n==0:
			print(ans)
		else:
			temp=[]
			for i in range(r):
				colcnt=arr[i][0]
				if colcnt%2==1:
					temp.append(arr[i][(colcnt//2)+1])
			temp=sorted(temp,reverse=True)
			if debug:
				print("temp",temp[:n:])
			print(ans+sum(temp[:2*n:2]))



while True:
	try:
		main(debug=False)
	except (ValueError,EOFError) as e:
		break