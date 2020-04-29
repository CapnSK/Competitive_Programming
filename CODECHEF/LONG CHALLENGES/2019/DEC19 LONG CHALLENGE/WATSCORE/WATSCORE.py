def main(debug=False):
	for _ in range(int(input())):
		n=int(input())
		mks={i:0 for i in range(1,9)}
		for i in range(n):
			sub,mk=map(int,input().split())
			if sub<9:
				mks[sub]=max(mks[sub],mk)
		
		arr=sorted(list(mks.values()),reverse=True)
		s=sum(arr[:len(arr):])
		print(s)

while True:
	try:
		main(debug=False)
	except (ValueError,EOFError) as e:
		break