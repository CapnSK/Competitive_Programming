x,y,gcd=0,0,0
def extendedEuclid(a,b):
	global x,y,gcd
	if b==0:
		x=1
		y=0
		gcd=a
		return
	extendedEuclid(b,a%b)
	cX=y
	cY=x-(a//b)*y
	x=cX
	y=cY
	return


def getModularInv(n,MOD):
	global x,y
	extendedEuclid(n,MOD)
	return x%MOD


def pow1(base,expo,MOD):
	ans=1

	while expo>0:
		if expo&1:
			ans = (ans*base)%MOD
		base=(base*base)%MOD
		expo=expo>>1
	return ans%MOD

def getProb(lseProb,operator,rseProb,debug):
	currProb=[0 for i in range(4)]
	if debug:
		print(lseProb,operator,rseProb)
	if operator=='&':
		currProb[0]=((lseProb[0]*rseProb[0])+(lseProb[0]*rseProb[1])+(lseProb[1]*rseProb[0])+(lseProb[0]*rseProb[2])+(lseProb[2]*rseProb[0])+(lseProb[2]*rseProb[3])+(lseProb[0]*rseProb[3])+(lseProb[3]*rseProb[0])+(lseProb[3]*rseProb[2]))
		currProb[1]=(lseProb[1]*rseProb[1])
		currProb[2]=((lseProb[1]*rseProb[2])+(lseProb[2]*rseProb[1])+(lseProb[2]*rseProb[2]))
		currProb[3]=((lseProb[1]*rseProb[3])+(lseProb[3]*rseProb[1])+(lseProb[3]*rseProb[3]))
	elif operator=='|':
		currProb[0]=(lseProb[0]*rseProb[0])
		currProb[1]=((lseProb[0]*rseProb[1])+(lseProb[1]*rseProb[0])+(lseProb[1]*rseProb[1])+(lseProb[1]*rseProb[2])+(lseProb[2]*rseProb[1])+(lseProb[2]*rseProb[3])+(lseProb[1]*rseProb[3])+(lseProb[3]*rseProb[1])+(lseProb[3]*rseProb[2]))
		currProb[2]=((lseProb[0]*rseProb[2])+(lseProb[2]*rseProb[0])+(lseProb[2]*rseProb[2]))
		currProb[3]=((lseProb[0]*rseProb[3])+(lseProb[3]*rseProb[0])+(lseProb[3]*rseProb[3]))
	elif operator=='^':
		currProb[0]=((lseProb[0]*rseProb[0])+(lseProb[1]*rseProb[1])+(lseProb[2]*rseProb[2])+(lseProb[3]*rseProb[3]))
		currProb[1]=((lseProb[0]*rseProb[1])+(lseProb[1]*rseProb[0])+(lseProb[2]*rseProb[3])+(lseProb[3]*rseProb[2]))
		currProb[2]=((lseProb[0]*rseProb[2])+(lseProb[2]*rseProb[0])+(lseProb[3]*rseProb[1])+(lseProb[1]*rseProb[3]))
		currProb[3]=((lseProb[0]*rseProb[3])+(lseProb[3]*rseProb[0])+(lseProb[2]*rseProb[1])+(lseProb[1]*rseProb[2]))

	if debug:
		print("curr prob in getprob",currProb)
	return currProb



def main(debug=False):
	MOD=998244353
	operators=['^','&','|']
	for _ in range(int(input())):
		l=input().strip()
		operandCount=l.count('#')
		Q=pow1(4,operandCount,MOD)
		Qinv=getModularInv(Q,MOD)
		stringStack=[]
		probStack=[]

		currInd=0

		if operandCount==1:
			print(*list(Qinv for i in range(4)))
		else:
			while currInd<len(l):
				currChar=l[currInd]
				if debug:
					print("Current Index is",currInd,"currChar is",currChar)
					print("Prob stack before",probStack)
				if currChar==')':
					#tmp=[]
					operator=''
					operands=0
					if debug:
						print("\tstringStack contents",stringStack)
					while stringStack[-1]!='(':
						ch=stringStack.pop()
						if debug:
							print("\t\tcurr chr is",ch)
						if ch=='#':
							operands+=1
						elif ch in operators:
							operator=ch
					stringStack.pop()
					popCount=2-operands
					currProb=[]
					if popCount==0:
						currProb=getProb([1,1,1,1],operator,[1,1,1,1],debug)
					elif popCount==1:
						currProb=getProb(probStack.pop(),operator,[1,1,1,1],debug)
					elif popCount==2:
						currProb=getProb(probStack.pop(),operator,probStack.pop(),debug)
					probStack.append(currProb)

				else:
					stringStack.append(currChar)
				currInd+=1
				if debug:
					print("Prob stack after",probStack)

			P=probStack.pop()
			finalOp=[(P[i]*Qinv)%MOD for i in range(4)]
			print(*finalOp)



while True:
	try:
		main(debug=False)
	except (EOFError,ValueError) as e:
		break