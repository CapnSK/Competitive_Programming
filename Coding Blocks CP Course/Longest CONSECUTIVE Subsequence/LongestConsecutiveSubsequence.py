'''
	This is the code for Longest Consecutive Subsequence in O(n) time using dictionary.
	Each LCS has Left Boundary and Right Boundary. Boundaries store sequence length and intermediate nodes store their occurence in the whole sequence.
	
	Sample test case:
	Input:	
		n -> 9
		arr -> 5 6 15 16 7 1 2 8 9
	Output:
		LCS length -> 5
	
	How?:
		Dictionary after iterating whole array:
			{1: 2, 2: 2, 5: 5, 6: 2, 7: 3, 8: 4, 9:5, 15: 2, 16: 2}
		Here there are 4 consecutive subsequences:
		Boundaries-> L R     L       R     L   R
		Keys->	     1,2     5,6,7,8,9     15,16
		Vals->	     2,2     5,2,3,4,5      2,2
		As you can see, Left Boundary and Right Boundary of the sequences store sequence length and intermediate nodes store occ in seq.

'''

n = int(input())
arr = list(map(int,input().split()))
d = {}
ans = 0
for i in range(n):
	element = arr[i]
	if element not in d:
		if element-1 in d and element+1 in d:
			lV = d[element-1]
			rV = d[element+1]
			d[element] = lV+1
			ans = max(ans,lV+rV+1)
			d[element-lV] = lV+rV+1
			d[element+rV] = lV+rV+1
		elif element-1 in d:
			lV = d[element-1]
			d[element] = lV+1
			d[element-lV] = lV+1
			ans = max(ans,lV+1)
		elif element+1 in d:
			rV = d[element+1]
			d[element] = rV+1
			d[element+rV] = rV+1
			ans = max(ans,rV+1)
		else:
			d[element] = 1

print(ans)
print(d)