def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1
n=int(input())
while(n>0):
	print(modInverse(n,pow(10,9)+7))
	n=int(input())