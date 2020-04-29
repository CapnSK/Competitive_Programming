from itertools import permutations
# def countSetBits(n):
# 	ans=0
# 	while n:
# 		p=n & (-n)
# 		n=n-p
# 		ans+=1
# 	return ans

def main(debug=False):
	for _ in range(int(input())):
		n=int(input())
		ab=input()
		bb=input()
		# ai=int(ab,2)
		# bi=int(bb,2)
		# setbitsA=countSetBits(ai)
		# setBitsB=countSetBits(bi)
		# if debug:
		# 	print("setBitsA and setBitsB",setbitsA,setBitsB)
		A=list(map(''.join,list(set(list(permutations(ab,n))))))
		B=list(map(''.join,list(set(list(permutations(bb,n))))))
		if debug:
			print("A",A)
			print("B",B)
		d={}
		cnt=0
		for i in A:
			for j in B:
				xor=int(i,2)^int(j,2)
				if xor not in d:
					d[xor]=1
					cnt+=1
		print(cnt)


while True:
	try:
		main(debug=False)
	except (ValueError,EOFError) as e:
		break