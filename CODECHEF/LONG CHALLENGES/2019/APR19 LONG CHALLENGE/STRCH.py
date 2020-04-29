while True :
	#try :
		for _ in range(int(input())):
			n=int(input())
			s,x=input().split()
			string=[[] for i in range(26)]
			frequency={}
			i=0
			for char in s:
				string[ord(char)-97].append(i)
				i+=1
				if char in frequency :
					frequency[char]+=1
				else :
					frequency[char] = 1
			print(string,frequency)



	#except :
	#	break