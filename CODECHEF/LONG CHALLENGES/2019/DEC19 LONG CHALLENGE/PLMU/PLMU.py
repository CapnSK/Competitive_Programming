from math import factorial
import operator as op
from functools import reduce


def nCr(n,r):
	if n<r:
		return 0
	r = min(r, n-r)
	numer = reduce(op.mul, range(n, n-r, -1), 1)
	denom = reduce(op.mul, range(1, r+1), 1)
	return numer // denom

def main(debug=False):
	for _ in range(int(input())):
		n=int(input())
		arr=list(map(int,input().split()))
		cnt2=arr.count(2)
		cnt0=arr.count(0)
		print(nCr(cnt2,2)+nCr(cnt0,2))


while True:
	try:
		main(debug=True)
	except (ValueError,EOFError) as e:
		break