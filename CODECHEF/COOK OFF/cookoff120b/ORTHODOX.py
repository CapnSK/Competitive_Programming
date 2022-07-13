import math
def main(debug=False):
	for _ in range(int(input())):
		n = int(input())
		arr = list(map(int,input().split()))
		bits = int(math.ceil(math.log(n,2)))

		if debug:
			print(bits)

		if bits>62:
			print("NO")
			continue
		ans = 0
		d = {}
		for i in range(n):
			for j in range(i,n):
				num=arr[i]
				if debug:
					print("i,j",i,j)
				for k in range(i,j+1):
					num = num|arr[k]
				if num not in d:
					d[num]=True
					ans+=1
				if debug:
					print(d)
		if debug:
			print(ans,n*(n+1)//2)
		print("YES" if ans==((n*(n+1))//2) else "NO")

		

while True:
	try:
		main(debug=False)
	except (EOFError,ValueError) as e:
		break