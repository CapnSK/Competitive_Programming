from itertools import combinations
def main(debug=False):
	for _ in range(int(input())):
		n=int(input())
		s=input().strip()
		found=False
		l=0
		for i in range(n-1,0,-1):
			combs=list(combinations(s,i))
			combs=list(map(''.join,combs))
			d={}
			for tmp in combs:
				if tmp not in d:
					d[tmp]=1
				else:
					found=True
					l=i
					break
			if found:
				break
		print(l)


while True:
	try:
		main(debug=False)
	except (ValueError,EOFError) as e:
		break