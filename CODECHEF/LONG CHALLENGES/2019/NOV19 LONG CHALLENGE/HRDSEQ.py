def main(debug=False):
	for _ in range(int(input())):
		n=int(input())
		visited=[False for i in range(1000)]
		LastOccured={}
		Count={}

		series=[0]
		#visited[0]=True
		#LastOccured[0]=0
		#Count[0]=1
		for i in range(1,n+1):
			l=series[-1]
			if debug:
				print("i :",i)
			if visited[l]:
				if debug:
					print("in if")
				l1=LastOccured[l]
				LastOccured[l]=i
				Count[l]+=1
				if debug:
					print("l1 i",l1,i)
				series.append(i-l1)
			else:
				if debug:
					print("in else")
				visited[l]=True
				LastOccured[l]=i
				Count[l]=1
				series.append(0)
			if debug:
				print("Count ", Count)
				print("series ",series)

		if debug:
			print(Count)
		print(Count[series[-2]])


while True:
	try:
		main(debug=False)
	except (ValueError,EOFError) as e:
		break