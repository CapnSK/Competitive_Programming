def main(debug=False):
	for _ in range(int(input())):
		s=input()
		ans=0
		i=0
		while i<len(s):
			if i+1<len(s) and s[i]=='x' and s[i+1]=='y':
				ans+=1
				i+=2
				continue
			elif i+1<len(s) and s[i]=='y' and s[i+1]=='x':
				ans+=1
				i+=2
				continue
			else:
				i+=1	
		print(ans)
while True:
	try:
		main(debug=True)
	except (ValueError,EOFError) as e:
		break