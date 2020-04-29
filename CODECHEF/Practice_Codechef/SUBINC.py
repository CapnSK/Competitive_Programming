while True:
	try:
		for _ in range(int(input())):
			n=int(input())
			a=list(map(int,input().split()))
			answer=0
			cnt=1

			for i in range(n-1):
				if a[i]<=a[i+1]:
					cnt=1
					while(i<n-1 and a[i]<=a[i+1]):
						cnt+=1
						i+=1

					answer+= (cnt*(cnt+1))//2
					cnt=1
			print(answer)

	except:
		raise