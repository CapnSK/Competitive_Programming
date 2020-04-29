import time

print("Enter the size of arrays")
n=int(input())            

print("Enter elements of array")

arr=[int(i) for i in input().strip().split()]     #Array  initialization phase
sumarr=[0 for i in range(n)]

sumarr[0]=arr[0]
print(sumarr)

for i in range(1,n):
	sumarr[i]=sumarr[i-1]+arr[i]
	time.sleep(2)
	print(sumarr)
