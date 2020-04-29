d={i-96:chr(i) for i in range(97,97+26)}
def getPerms(s,op,pos,arr,slen):
	global d
	if pos==slen:
		arr.append(op)
		return
	getPerms(s,op+d[int(s[pos])],pos+1,arr,slen)
	if pos+1<slen and int(s[pos]+s[pos+1]) in d:
		getPerms(s,op+d[int(s[pos]+s[pos+1])],pos+2,arr,slen)
	

s=input()
A=[]
getPerms(s,'',0,A,len(s))
print('[',end='')
for i in range(len(A)-1):
	print(A[i]+', ',end='')
print(A[-1]+']')