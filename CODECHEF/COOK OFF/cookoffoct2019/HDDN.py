from bisect import bisect_left,bisect_right
def main(debug=False):
	for _ in range(int(input())):
		n,k,m = map(int,input().split())

		seq=[-1 for i in range(n+1)]

		freq={}
		lastOccured={i:[] for i in range(0,n+1)}
		last={i:0 for i in range(1,k+1)}
		XYZ=[]
		for i in range(m):
			XYZ.append(list(map(int,input().split())))

		XYZ = sorted(XYZ,key=lambda x:x[2])
		if debug:
			print("sorted XYZ",XYZ)
		possible = True
		for i in range(m):
			x,y,z=XYZ[i]
			if debug:
				print("FOR ",x,y,z)
			if y>z:
				if debug:
					print("y>z")
				possible=False
				break
			if seq[z]!=-1:
				if debug:
					print("seq[z]!=-1")
				possible=False
				break
			xfreq=-1
			if x in freq:
				xfreq=freq[x]
				freq[x]+=1
			else:
				xfreq=y-1
				freq[x]=y
			if xfreq!=y-1:
				if debug:
					print("xfreq!=y-1",xfreq,y-1)
				possible=False
				break
			seq[z]=x
			j=1
			cnt=xfreq
			while j<z and cnt>0:
				if seq[j]==-1:
					seq[j]=x
					cnt-=1
				j+=1
			
			last[x]=z
			#lastOccured[z]=x
			# for k in lastOccured:
			# 	if k<z:
			# 		if lastOccured[k]==x:
			# 			lastOccured[k]=0
			# 			break
			# 	else:
			# 		break

			if debug:
				print("last :",last)
				print("FINAL SEQ IS: ",seq)

		#l=sorted(list(last.values()))
		if debug:
			print("lastOccured Before:",lastOccured)
		temp=list(last.items())
		for i in range(len(temp)):
			k,v=temp[i]
			# if debug:
			# 	print("i,k,v is",i,k,v)
			#t=temp[i-1][1]
			#lastOccured[v]+=t
			lastOccured[v].append(k)

		# prev=[]
		# for k in lastOccured:
		# 	lastOccured[k]+=prev
		# 	prev=lastOccured[k]
		if debug:
			print("lastOccured After:",lastOccured)
			print("Seq Before",seq[1::])
		if not possible:
			print("No")
		else:
			for i in range(1,n+1):
				if seq[i]==-1:
					if len(lastOccured[0])>0:
						seq[i]=lastOccured[0][0]
					else:
						possible=False
						for j in range(i-1,0,-1):
							if len(lastOccured[j])>0:
								seq[i]=lastOccured[j][0]
								possible=True
								break
			possible=True
			for i in range(1,n+1):
				if seq[i]==-1:
					possible=False
					break
			if possible:
				print("Yes")
				print(*seq[1::])
			else:
				print("No")

while True:
	try:
		main(debug=False)
	except (ValueError,EOFError) as e:
		break