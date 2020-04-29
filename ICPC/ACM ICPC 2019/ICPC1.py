while True:
	for _ in range(int(input())):
		s,t = input().split()

		count = {}
		for ss in s:
			if ss not in count:
				count[ss] = 1
			else:
				count[ss] += 1