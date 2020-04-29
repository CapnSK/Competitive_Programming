for _ in range(int(input())):
	String = "AEIOUaeiou"
	stri = input()
	cnt = 0
	for s in stri:
		if s in String:
			cnt+=1
	print(cnt)