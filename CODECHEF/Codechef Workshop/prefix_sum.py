import time

print("Enter the size of arrays")
n=int(input())            

print("Enter elements of array")

arr=[int(i) for i in input().strip().split()]     #Array  initialization phase
sumarr=[0 for i in range(n)]

sumarr[0]=arr[0]
print("Regular Array",arr)
print("Prefix Array",sumarr)
time.sleep(2)
print("\n\n")


for i in range(1,n):
	print("Iteration ",i,"\n")
	sumarr[i]=sumarr[i-1]+arr[i]
	time.sleep(2)
	print("Regular Array",arr)
	print("Prefix Array",sumarr)
	print("\n\n")


print("Enter the index you want to access")
key=int(input())

print(sumarr[key]-sumarr[key-1])
print(arr[key])