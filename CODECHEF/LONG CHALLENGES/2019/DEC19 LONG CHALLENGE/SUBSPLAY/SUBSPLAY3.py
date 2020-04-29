def main(debug=False):
	for _ in range(int(input())):
		n=int(input())
		s=input().strip()
		d={}
		ans=0
		for i in range(n):
			if s[i] in d:
				ans=max(ans,n-(i-d[s[i]]))
			d[s[i]]=i
		print(ans)
while True:
	try:
		main(debug=False)
	except (ValueError, EOFError) as e:
		break