
def getWinner(teams,a):
	b = []
	if len(a) == 1:
		return a[0]
	for i in range(0,len(a),2):
		cnta = 0
		cntb = 0
		for j in range(5):
			if teams[a[i] - 1][j]>teams[a[i + 1] - 1][j]:
				cnta+=1
			if teams[a[i] - 1][j]<teams[a[i+1] - 1][j]:
				cntb+=1
			if teams[a[i] - 1][j] == teams[a[i+1] - 1][j]:
				cnta+=1

			if cnta == 3:
				b.append(a[i])
				break
			elif cntb == 3:
				b.append(a[i+1])
				break

	return getWinner(teams,b)


for _ in range(int(input())):
	n = int(input())
	teams = []
	for __ in range(n):
		teams.append(list(map(int,input().split())))

	print(getWinner(teams,range(1,n+1)))