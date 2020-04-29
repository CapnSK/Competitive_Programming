def poss(n):
	if abs(n)&1 or abs(n)%4==0:
		return True
	return False
def main(debug=False):
	#precompute()
	for _ in range(int(input())):
		n=int(input())
		arr=list(map(int,input().split()))
		premul=[1]
		for i in range(n):
			premul.append(premul[-1]*arr[i])
		if debug:
			print("premul",premul)
		cnt=0
		for i in range(n+1):
			for j in range(i+1,n+1):
				if debug:
					print("mul from ",i,"to",j,"is",premul[j]//premul[i],arr[i:j])
				if poss(premul[j]//premul[i]):
					cnt+=1
				if debug:
					print("count",cnt)
		print(cnt)
while True:
	try:
		main(debug=True)
	except (ValueError,EOFError) as e:
		break

'''
	# if len(mods[0])==0 and len(mods[2])>2:
	# 	for i in range(len(mods[2])-1):
	# 		start=mods[2][i]
	# 		prev=mods[2][i-1] if i-1>=0 else -1
	# 		end=mods[2][i+1] if mods[2][i+1]<n else n-1
	# 		ans+= (start-prev)*(n-end)
	# 		#print(prev,start,end,ans)

	# elif len(mods[0])>0 and len(mods[2])<2:
	# 	for i in range(len(mods[0])):
	# 		curr=mods[0][i]
	# 		prev=mods[0][i-1] if i-1>=0 else -1
	# 		ans+= (curr-prev)*(n-curr)
		
	# elif len(mods[0])>0 and len(mods[2])>2:
	# 	for i in range(len(mods[2])-1):
	# 		start=mods[2][i]
	# 		prev=mods[2][i-1] if i-1>=0 else -1
	# 		end=mods[2][i+1] if mods[2][i+1]<n else n-1
	# 		ans+= (start-prev)*(n-end)
	# 	if debug:
	# 		print("before 4",ans)

	# 	for i in range(len(mods[0])):
	# 		curr=mods[0][i]
	# 		tmp=bisect_left(mods[2],mods[0][i])
	# 		if debug:
	# 			print(tmp)
	# 		prev2ind=mods[2][tmp-2] if tmp-2>=0 else -1
	# 		prev4ind=mods[0][i-1] if i-1>=0 else -1
	# 		if debug:
	# 			print("prev 2 4",prev2ind,prev4ind)
	# 		prevInd=max(prev2ind,prev4ind)
	# 		#next2ind=mods[2][tmp+1] if tmp+1<len(mods[2]) else n-1
	# 		#next4ind=mods[0][i+1] if i+1<len(mods[0]) else n-1
	# 		#print("next 2 4",next2ind,next4ind)
	# 		nextInd=mods[2][tmp+1] if tmp+1<len(mods[2]) else n-1
	# 		ans+= (curr-prevInd)*(nextInd-curr)
	# 		if debug:
	# 			print("prev curr next ans",prevInd,curr,nextInd,ans)

	# if debug:
	# 	print("Final get4Count",ans)
'''