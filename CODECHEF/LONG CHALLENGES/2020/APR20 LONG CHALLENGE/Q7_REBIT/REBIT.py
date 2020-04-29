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

combs={'0':{'0':{'^':1,'&':4,'|':1},'1':{'^':1,'&':0,'|':1},'a':{'^':1,'&':0,'|':1},'A':{'^':1,'&':0,'|':1}},  '1':{'0':{'^':1,'&':1,'|':0},'1':{'^':1,'&':1,'|':4},'a':{'^':1,'&':1,'|':0},'A':{'^':1,'&':1,'|':0}},  'a':{'0':{'^':1,'&':2,'|':0},'1':{'^':1,'&':0,'|':2},'a':{'^':1,'&':2,'|':2},'A':{'^':1,'&':0,'|':0}},  'A':{'0':{'^':1,'&':2,'|':0},'1':{'^':1,'&':0,'|':2},'a':{'^':1,'&':0,'|':0},'A':{'^':1,'&':2,'|':2}}}

def getProb(prevProb,op,MOD,q,debug):
	global combs
	options=['0','1','a','A']
	currProb1=[0 for i in range(4)]
	currProb2=[0 for i in range(4)]
	for i in range(4):
		currProb1[i]=prevProb[i]*(combs['0'][options[i]][op]+combs['1'][options[i]][op]+combs['a'][options[i]][op]+combs['A'][options[i]][op])
		currProb2[i]=prevProb[i]*(combs[options[i]]['0'][op]+combs[options[i]]['1'][op]+combs[options[i]]['a'][op]+combs[options[i]]['A'][op])
		currProb1[i]%=MOD
		currProb2[i]%=MOD
		if debug:
			print("for",options[i],"prob is",currProb1[i],currProb2[i])

	if sum(currProb1)==q:
		return currProb1
	else:
		return currProb2

def main(debug=False):
	MOD=998244353
	operators=['^','&','|']
	for _ in range(int(input())):
		l=input().strip()
		operandCount=l.count('#')
		Q=pow1(4,operandCount,MOD)
		Qinv=getModularInv(Q,MOD)
		if debug:
			print("Q inverse",Qinv)
		if operandCount==1:
			print(*[Qinv for i in range(4)])
			continue
		else:
			currInd=0
			stack=[]
			probsStack=[[1,1,1,1]]
			q=4
			while currInd<len(l):
				currChar=l[currInd]
				if debug:
					print("Current index",currInd,"curr char is",currChar)
					print("Probabilities before",probsStack)


				if currChar=="(":
					stack.append(currChar)
					currInd+=1


				elif currChar==")":
					operator=''
					while stack[-1]!='(':
						tmp=stack.pop()
						if tmp in operators:
							operator=tmp
					q=(q*4)%MOD
					prevProb=probsStack.pop()
					currProb=getProb(prevProb,operator,MOD,q,debug)
					probsStack.append(currProb)

					if debug:
						print("currProb in main",currProb)
					currInd+=1
					prevProb=currProb


				elif currChar=="#":
					stack.append(currChar)
					currInd+=1


				elif currChar in operators:
					stack.append(currChar)
					currInd+=1

				if debug:
					print("Probabilities after",currProb)

			finalOuput=[(probsStack[-1][i]*Qinv)%MOD  for i in range(4)]
			print(*finalOuput)

while True:
	try:
		main(debug=True)
	except (EOFError,ValueError) as e:
		break