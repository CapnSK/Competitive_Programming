for _ in range(int(input())):
    n,m=map(int,input().split())
    xyf=input().split()
    x0,y0=int(xyf[0]),int(xyf[1])
    face=xyf[2]
    flag=False
    operations = input()
    
    for current in operations:
        if x0 > n or y0 > m or x0 < 1 or y0 < 1 :
            flag=True
            break
        else :
            if current == 'F':
                if face == 'N' :
                    y0+=1
                elif face == 'S' :
                    y0-=1                    
                elif face == 'W' :
                    x0-=1
                elif face == 'E' :
                    x0+=1                    
                
            elif current == 'R':
                if face == 'N' :
                    face = 'E'
                elif face == 'S' :
                    face = 'W'                    
                elif face == 'W' :
                    face = 'N'
                elif face == 'E' :
                    face = 'S' 
            elif current == 'L' :
                if face == 'N' :
                    face = 'W'
                elif face == 'S' :
                    face = 'E'                    
                elif face == 'W' :
                    face = 'S'
                elif face == 'E' :
                    face = 'N'
                    
        if x0 > n or y0 > m or x0 < 1 or y0 < 1 :
            flag=True
            break
    
    if flag :
        print(-1)
        continue
    else :
        print(x0,y0)