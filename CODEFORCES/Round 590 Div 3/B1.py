n,k = map(int,input().split())
convs = list(map(int,input().split()))

window = []

for i in convs:
	if len(window)>=k:
		if i not in window:
			del window[0]
			window.append(i)
	else:
		if i not in window:
			window.append(i)
print(len(window))
print(*window[::-1])