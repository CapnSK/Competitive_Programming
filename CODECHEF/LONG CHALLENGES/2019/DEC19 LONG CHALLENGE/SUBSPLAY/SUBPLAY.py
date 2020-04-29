from math import log2

def getSubSeqs(s,bits):
	global debug1
	subs={}
	for i in range(2**bits -1,-1,-1):
		bi=(bin(i)[2::]).rjust(bits,'0')
		tmp=''
		cnt=0
		for j in range(bits):
			if bi[j]=='1':
				tmp+=s[j]
				cnt+=1
		if cnt not in subs:
			subs[cnt]={}
		if tmp not in subs[cnt]:
			subs[cnt][tmp]=0
		subs[cnt][tmp]+=1
		if debug1:
			print("\nfor i=",bi,"dic is",subs)
		if subs[cnt][tmp]>=2:
			return cnt
	return 0

def getk(s,n):
	bits=n
	k=getSubSeqs(s,bits)
	return k

debug1=False
def main(debug=False):
	global debug1
	debug1=debug
	for _ in range(int(input())):
		n=int(input())
		s=input().strip()
		ans=getk(s,n)
		print(ans)

while True:
	try:
		main(debug=False)
	except (ValueError,EOFError) as e:
		break