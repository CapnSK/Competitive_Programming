def main(debug=False):
	for _ in range(int(input())):
		n,m=map(int,input().split())
		boxes=list(map(int,input().split()))
		box={}
		d={}
		Min={}
		Max={}
		for i in range(n):
			#box.append([boxes[i],i%m])
			if boxes[i] not in box:
				box[boxes[i]]=[]
			if i%m not in d:
				d[i%m]=[]
			if i%m not in Min:
				Min[i%m]=10**9 +1
			if i%m not in Max:
				Max[i%m]=-1
			box[boxes[i]].append(i%m)
			d[i%m].append(boxes[i])
			if Min[i%m]>boxes[i]:
				Min[i%m]=boxes[i]
			if Max[i%m]<boxes[i]:
				Max[i%m]=boxes[i]

		if debug:
			print("d",d)
			print("box",box)
			print("Min",Min)
			print("Max",Max)

		

while True:
	try:
		main(debug=True)
	except (ValueError,EOFError) as e:
		break