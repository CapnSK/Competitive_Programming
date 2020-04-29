def a(n):
	if n>50:
		return n-2
	return a(a(n+10))

print(a(30))