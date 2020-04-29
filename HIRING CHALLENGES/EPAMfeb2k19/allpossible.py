from itertools import permutations

permlist=permutations(input())

for i in list(permlist):
	print(''.join(i))