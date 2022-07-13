'''
	Problem Link: https://codeforces.com/contest/339/problem/D
	Verdict : TLE
	Remarks : Used Segment Trees still got tle maybe python issue!
'''


def build(ST,arr,n,ss,se,nodeInd,debug):
	if ss==se:
		if debug:
			print("Base Case")
			print("ss nodeInd",ss,nodeInd)
		ST[nodeInd] = (arr[ss],'or')
		return
	mid = (ss+se)//2
	build(ST,arr,n,ss,mid,2*nodeInd+1,debug)
	build(ST,arr,n,mid+1,se,2*nodeInd+2,debug)
	lval,op1 = ST[2*nodeInd +1]
	rval,op2 = ST[2*nodeInd +2]
	if op1==op2:
		if op1=='or':
			v = lval | rval
			ST[nodeInd] = (v,'xor') 
		elif op1=='xor':
			v = lval ^ rval
			ST[nodeInd] = (v,'or')
	return

def update(ST,arrInd,val,ss,se,nodeInd,debug):
	if ss>arrInd or se<arrInd:
		return
	if ss==se and ss==arrInd:
		ST[nodeInd] = (val,'or')
		return
	mid = (ss+se)//2
	update(ST,arrInd,val,ss,mid,2*nodeInd+1,debug)
	update(ST,arrInd,val,mid+1,se,2*nodeInd+2,debug)
	lval,op1 = ST[2*nodeInd +1]
	rval,op2 = ST[2*nodeInd +2]
	if op1==op2:
		if op1=='or':
			v = lval | rval
			ST[nodeInd] = (v,'xor') 
		elif op1=='xor':
			v = lval ^ rval
			ST[nodeInd] = (v,'or')
	return
debug = False
n,q = map(int,input().split())
e = 1<<n
arr = list(map(int,input().split()))
ST = [0]*(4*e)
build(ST,arr,n,0,e-1,0,debug)
if debug:
	print("ST",ST)
for i in range(q):
	p,b = map(int,input().split())
	update(ST,p-1,b,0,e-1,0,debug)
	print(ST[0][0])