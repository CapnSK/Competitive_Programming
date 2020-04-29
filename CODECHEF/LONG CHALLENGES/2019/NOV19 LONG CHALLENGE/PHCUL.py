from bisect import bisect_left,bisect_right

def lexSort(arr):
	arr=sorted(arr,key=lambda x:x[0])
	d={}
	for k,v in arr:
		if k in d:
			d[k].insert(bisect_left(d[k],v),v)
		else:
			d[k]=[v]
	newArr=[]
	for k in d:
		temp=d[k]
		for v in temp:
			newArr.append([k,v])
	return newArr

from math import sqrt

def euclid(P1,P2):
	x1,y1=P1
	x2,y2=P2

	return sqrt(((abs(x2-x1)**2)+(abs(y2-y1)**2)))

def main(debug=False):
	for _ in range(int(input())):
		x,y=map(int,input().split())
		A=[x,y]
		N,M,K=map(int,input().split())
		nt=list(map(int,input().split()))
		mt=list(map(int,input().split()))
		kt=list(map(int,input().split()))

		n=[[nt[i],nt[i+1]] for i in range(0,(2*N)-1,2)]
		m=[[mt[i],mt[i+1]] for i in range(0,(2*M)-1,2)]
		k=[[kt[i],kt[i+1]] for i in range(0,(2*K)-1,2)]


		if debug:
			print("n",n)
			print("m",m)
			print("k",k)

		an={}
		am={}
		nm={}
		mn={}
		nk={}
		mk={}

		for i in n:
			i=(i[0],i[1])
			if i not in an:
				an[i]=euclid(i,A)
		for i in m:
			i=(i[0],i[1])
			if i not in am:
				am[i]=euclid(i,A)

		an=sorted(list(an.items()),key=lambda x:x[1])
		am=sorted(list(am.items()),key=lambda x:x[1])

		if debug:
			print("an",an)
			print("am",am)


		for i in n:
			i=(i[0],i[1])
			nm[i]=[i,10**9 + 1]
			for j in m:
				j=(j[0],j[1])
				temp=euclid(i,j)
				if temp<nm[i][1]:
					nm[i]=[j,temp]

		for i in m:
			i=(i[0],i[1])
			mn[i]=[i,10**9 + 1]
			for j in n:
				j=(j[0],j[1])
				temp=euclid(i,j)
				if temp<mn[i][1]:
					mn[i]=[j,temp]


		for i in m:
			i=(i[0],i[1])
			mk[i]=[i,10**9 + 1]
			for j in k:
				j=(j[0],j[1])
				temp=euclid(i,j)
				if temp<mk[i][1]:
					mk[i]=[j,temp]
		for i in n:
			i=(i[0],i[1])
			nk[i]=[i,10**9 + 1]
			for j in k:
				j=(j[0],j[1])
				temp=euclid(i,j)
				if temp<nk[i][1]:
					nk[i]=[j,temp]

		if debug:
			print("mn",mn)
			print("nm",nm)
			print("mk",mk)
			print("nk",nk)

		
		d=10**9 + 1

		for pt,dist in an:
			d1=dist
			if pt in nm:
				d2=nm[pt][1]
				pt2=nm[pt][0]
				if pt2 in mk:
					d3=mk[pt2][1]
					pt3=mk[pt2][0]
					if debug:
						print("for",pt,pt2,pt3,d1+d2+d3)
					d=min(d,d1+d2+d3)
			#d=min(d,dist+nm[pt][1]+mk[nm[pt][0]][1])

		for pt,dist in am:
			d1=dist
			if pt in mn:
				d2=mn[pt][1]
				pt2=mn[pt][0]
				if pt2 in nk:
					d3=nk[pt2][1]
					pt3=nk[pt2][0]
					if debug:
						print("for",pt,pt2,pt3,d1+d2+d3)
					d=min(d,d1+d2+d3)
			#d=min(d,dist+mn[pt][1]+nk[mn[pt][0]][1])

		print(d)


while True:
	try:
		main(debug=False)
	except (ValueError,EOFError) as e:
		break