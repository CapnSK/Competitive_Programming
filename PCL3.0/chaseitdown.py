for _ in range(int(input())):
	target,max_overs=map(int,input().split())
	played_overs=0
	total_runs=0
	data=[]
	for i in range(11):
		data.append(list(map(int,input().split())))
	for runs,overs in data :
		can_play_overs=min(overs,max_overs-played_overs)
		played_overs+=can_play_overs
		total_runs+=(runs*can_play_overs)
		if played_overs == max_overs :
			break

	if total_runs >= target :
		print("Y",total_runs)
	else :
		print("N",-1)