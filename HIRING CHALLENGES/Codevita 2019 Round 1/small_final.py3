n = int(input())
string = input().strip()
c=[0 for i in range(n)]
a=[0 for i in range(26)]

for i in range(len(string)):
	x=string[i]
	a[ord(x)-97]+=1
	c[i]=a[ord(x)-97]
q=int(input())

for i in range(q):
	m=int(input())
	m=m-1
	print(c[m]-1 )