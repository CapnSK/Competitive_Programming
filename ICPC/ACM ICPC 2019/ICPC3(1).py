t=int(input())

while(t>0):
    n=int(input())
    l=[]

    for i in range(n):
        L,R,V=map(int,input().split())
        l.append([L,R,V])
        #v.append(V)
    ans="YES"
    notpos=False
    for i in range(n):
        L1=l[i][0]
        R1=l[i][1]
        V1=l[i][2]
        cnt=0
        ind=[]
        for j in range(n):
            if j!=i:
                L2=l[j][0]
                R2=l[j][1]
                V2=l[j][2]
                if V1==V2:
                    if (L1>=L2 and R1<=R2) or (L1<=L2 and R1>=R2) or (L1<=L2 and R1<=R2) or (L2<=L1 and R2<=R1):
                        ind.append(j)
                        cnt+=1
                if cnt>=2:
                    print(i,ind)
                    notpos=True
                    break
        #print(cnt)
        if notpos==True:
            ans="NO"
            break
    print(ans)
    t-=1