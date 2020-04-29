for _ in range(int(input())+1):
            rows,cols=map(int,input().split())
            globe=[]
            offices=[]
            manhattan_distances=[]
            for i in range(rows):
                manhattan_distances.append([-1 for j in range(cols)])



            for i in range(rows):
                temp_row=[int(k) for k in input()]                           
                globe.append(temp_row)

                for j in range(cols):
                    if temp_row[j]==1 :
                        offices.append([i,j])
                        manhattan_distances[i][j]=0



            for i in range(rows):
                for j in range(cols):
                    min_dist=999999999999
                    for r,c in offices:
                        dist=abs(r-i)+abs(c-j)
                        if dist<min_dist:
                            min_dist=dist
                    manhattan_distances[i][j]=min_dist
            print("before",globe,offices,manhattan_distances)
            #print(max(max(manhattan_distances)))
            r=manhattan_distances.index(max(manhattan_distances))
            c=manhattan_distances[r].index(max(manhattan_distances[r]))
            #print(r,c)




            globe[r][c]=1
            offices.append([r,c])



            for i in range(rows):
                for j in range(cols):
                    #min_dist=999999999999
                    #for r,c in offices:
                    dist=abs(r-i)+abs(c-j)
                    if manhattan_distances[i][j]>dist:
                            manhattan_distances[i][j]=dist
       


            print("After",globe,offices,manhattan_distances)
            print("Case #",_+1,":",sep="",end=" ")
            print(max(max(manhattan_distances)))


