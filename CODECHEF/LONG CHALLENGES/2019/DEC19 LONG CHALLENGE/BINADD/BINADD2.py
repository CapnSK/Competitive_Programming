def main(debug=False):
	for _ in range(int(input())):
		a=input().strip()
		b=input().strip()
		a=a[::-1]
		b=b[::-1]
		while len(a)<len(b):
			a+='0'
		while len(b)<len(a):
			b+='0'

		if debug:
			print(a,b)

		carry,ans,cur=0,0,0


		for i in range(len(a)):
			carry= carry+int(a[i])+int(b[i])
			if debug:
				print("For i=",i,"a[i] b[i]",a[i],b[i])
			if carry==2:
				cur+=1
			else:
				cur=carry//2
			if debug:
				print("carry",carry)
				print("Curr",cur)
			carry= int(carry/2)
			ans=max(ans,cur+1)
			if debug:
				print("Ans",ans)

		
		if b.count('1')>0:
			print(ans)
		else:
			print(0)


while True:
	try:
		main(debug=False)
	except (ValueError,EOFError) as e:
		break