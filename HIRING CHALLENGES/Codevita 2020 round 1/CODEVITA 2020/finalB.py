def isPrime(no): 						#Checks Prime Number - function
    ptr=2
    while(ptr*ptr<=no):
        if(no % ptr == 0):
            return False 				#false means Number is not a prime no
        ptr+=1
    return True   						# True means Number is a prime no

def main():
    D,P=map(int,input().split())        #Take the input
    noOfParts=int(D/P)                  #Total no of parts to be Divided    
    primeInsatanceNo=0
    for no in range(2,noOfParts+1):
        cnt=0                           
        while(isPrime(no) and no<=D):   
            cnt+=1
            no+=noOfParts

        if(cnt==P):
            primeInsatanceNo+=1
    
    print(primeInsatanceNo)            	 #Final Answer

main()