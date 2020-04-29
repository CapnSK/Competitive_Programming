t=int(input())
for x in range(t):
    a,b=list(map(int,input().split()))
    n=10
    c=0
    d=0
    sum2=0
    k=''
    while(a!=0 and b!=0):
        c=a%n
        a=a//n
        d=b%n
        b=b//n
        if (c+d)>=10:
            sum2=(c+d)-10
            k=str(sum2)+k
        else: 
             k=str(c+d)+k
    max1=max(a,b)
    if max1!=0:
        print(int(str(max1)+k))         
    else: print(int(k))        
