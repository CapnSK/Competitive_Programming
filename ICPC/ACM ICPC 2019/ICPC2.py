t=int(input())

while(t>0):
    n=int(input())
    a={}
    for i in range(n):
        w,s=map(str,input().split())
        x=int(s)
        #print(w,x)
        if w not in a:
            a[w]=[0,0]
            a[w][x]+=1
        else:
            a[w][x]+=1
    sum1=0
    for i in a:
        sum1+=max(a[i][0],a[i][1])
    print(sum1)


    t-=1