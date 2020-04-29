while True:
	try:
		for _ in range(int(input())):
			n = int(input())
			Temp,DP = {},{}
			inputs = []
			for _ in range(n):
				b,num = input().split()
				inputs.append((int(b),num))
			inputs = list(set(inputs))
			n = len(inputs)
			for i in inputs:
				Temp = {}
				if i[0] == -1:
					minbase = max(i[1])
					minbase = max(int(minbase,36) + 1,2)
					#print('minbase ',i[1],minbase)
					for j in range(minbase,37):
						#print( int(i[1], j))
						if int(i[1],j) not in Temp:
							Temp [int(i[1],j)] = 1
						else:
							Temp [int(i[1],j)] += 1
						#print(Temp)
					for k,v in Temp.items():
						if k not in DP:
							DP[k] = 1
						else:
							DP[k] += 1
				else:
					if int(i[1], i[0])not in DP:
						DP[ int(i[1],i[0]) ] = 1
					else:
						DP[ int(i[1],i[0]) ] += 1

			GotAns = False
			#print(DP)
			DP = sorted(DP.items(),key = lambda x : x[0])
			for k,v in DP:
				if v == n:
					if k > 1000000000000:
						break
					else:
						GotAns = True
						print(k)
						break
			if not GotAns:
				print(-1)

	except:
		break