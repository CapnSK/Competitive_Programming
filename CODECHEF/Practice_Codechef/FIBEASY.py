
def create(n):
	arr=[]
	arr.append(0)
	arr.append(1)
	for i in range(n-2):
		arr.append((arr[-1]+arr[-2])%10)
	return arr
for _ in range(int(input())):
	
	digits=create(60)

	n=int(input())
	
	gapi=0
	gap = 2**gapi
	arr_size=n
	last_index = n-1
	while arr_size>1:
		#print("BEFORE ",arr_size,":",last_index,"|||",gap)
		if arr_size%2==1:
			last_index-=gap
		gapi+=1
		gap=2**gapi
		arr_size= arr_size//2
		#print("AFTER ",arr_size,":",last_index,"|||",gap)
		#print(end="\n\n")

	print(digits[(last_index)%60])