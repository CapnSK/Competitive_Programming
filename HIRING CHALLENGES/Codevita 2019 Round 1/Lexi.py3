t=int(input())
for _ in range(t):
	order = input().strip()
	sample = input().strip()

	alpha = {chr(i):0 for i in range(97,123)}

	for i in sample:
		alpha[i]+=1

	ans = ''

	for i in order:
		ans+=i*alpha[i]
	print(ans,end='')
	if _==t-1:
		break
	print()