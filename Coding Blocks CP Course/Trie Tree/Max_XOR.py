'''
	This code is to find out the max xor pair in array using a trie tree in O(32*n) time.
	32 beacause assuming the integer is 32 bit.
'''

class node:
	def __init__(self):
		self.left = None     # Left node indicates presence of bit 0
		self.right = None	 # Right node indicates presence of bit 1

class Trie:
	def __init__(self):
		self.root = node()

	def insert(self,n:int):
		temp = self.root
		#Int is 32 bit: Assume, so iterate through all bits and build a trie based on its binary representation
		for i in range(31,-1,-1):
			bit = (n>>i)&1         #ith bit extracted
			if bit==0:  
				if temp.left is None:  # If no 0 bit is present
					temp.left = node()
				temp = temp.left
			else:
				if temp.right is None: # If no 1 bit is present
					temp.right = node()
				temp = temp.right

	def MaxXorHelper(self,value:int):
		temp = self.root
		curr_ans = 0
		for i in range(31,-1,-1):
			bit = (value>>i)&1
			if bit==0:               # If bit is 0 we have to find if current node has a right node that is bit as 1 to maximize xor.
				if temp.right is not None:
					temp = temp.right
					curr_ans += (1<<i)  #If bit 1 is present so xor will be 1 therefor ans will increase by 2^i
				else:
					temp = temp.left
			else:                    # If bit is 1 we have to find if current node has a left node that is bit as 0 to maximize xor.
				if temp.left is not None:
					temp = temp.left
					curr_ans += (1<<i)  #If bit 0 is present so xor will be 1 therefor ans will increase by 2^i
				else:
					temp = temp.right
		return curr_ans

	def maxXor(self,arr,n):
		max_xor = 0
		for num in arr:
			self.insert(num)             # first insert the number
			ans = self.MaxXorHelper(num) # then calculate max xor possible with this number and numbers present in array till now
			print("intermediate ans for",num,"is",ans)  # for debug purpose, comment out if not needed
			max_xor = max(max_xor,ans)   # Choose whichever value is max

		return max_xor

t = Trie()
n = int(input())
arr = list(map(int,input().split()))
print(t.maxXor(arr,n))