def main(debug=False):
	for _ in range(int(input())):
		n=int(input())
		l=len(str(n))
		ans=0
		for i in range(1,l):
			ans+= 1<<i
			if debug:
				print(ans)

		a=''
		for i in str(n):
			if i=='4':
				a+='0'
			else:
				a+='1'
		print(ans+int(a,2)+1)

main(debug=False)