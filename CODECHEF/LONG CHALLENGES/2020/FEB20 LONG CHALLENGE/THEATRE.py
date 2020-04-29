def main(debug=False):
	Ans=0
	for _ in range(int(input())):
		n=int(input())
		d={'A':{},'B':{},'C':{},'D':{}}
		for i in range(n):
			m,t=input().split()
			t=int(t)
			if t not in d[m]:
				d[m][t]=0
			d[m][t]+=1
		if debug:
			print(*list(d.items()),sep="\n")
			print("d['A']",d['A'])

		# m1=max(list(d['A'].items()),key=lambda x:x[1])[1]
		# m2=max(list(d['B'].items()),key=lambda x:x[1])[1]
		# m3=max(list(d['C'].items()),key=lambda x:x[1])[1]
		# m4=max(list(d['D'].items()),key=lambda x:x[1])[1]
		arr=[]
		for k in d:
			if len(d[k])>0:
				arr.append(max(list(d[k].items()),key=lambda x:x[1])[1])
		arr.sort(reverse=True)

		if debug:
			print("Arr",arr)
		while len(arr)<4:
			arr.append(0)
		
		c=0
		for i in arr:
			if i==0:
				c+=1
		res=arr[0]*100 + arr[1]*75 + arr[2]*50 + arr[3]*25 - c*100
		if debug:
			print("c",c)
		Ans+=res
		print(res)
	print(Ans)

while True:
	try:
		main(debug=False)
	except (EOFError,ValueError) as e:
		break