while True:
	try:
		n=int(input())
		for _ in range(n):
			s=input().strip()
			slen=len(s)
			places=[0 for i in range(slen)]
			doomed=False
			for i in range(slen):
				char=s[i]
				if char=='.':
					continue
				else:
					hops=int(char)
					lrange=max(0,i-hops)
					rrange=min(slen-1,i+hops)
					for j in range(lrange,rrange+1):
						places[j]+=1
						if places[j]>1:
							doomed=True
							break
					if doomed:
						break
			print("unsafe" if doomed else "safe")

	except:
		break