import time
start_time=0

def main():
	global start_time
	n,m=map(int,input().split())
	arr=list(map(int,input().split()))
	start_time = time.time()
	final=[0 for i in range(n)]
	for i in range(n):
		final[(i+n-m)%n]=arr[i]
	print(*final,sep=' ')


main()
print("--- %s seconds ---" % (time.time() - start_time))