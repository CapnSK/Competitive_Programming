def nCr(n, r): 
  
    return (fact(n) / (fact(r) * fact(n - r))) 

def fact(n):
    res = 1
      
    for i in range(2, n+1): 
        res = res * i 
          
    return res 


while True:
    try:
        for _ in range(int(input())):
            r,c = map(int,input().split())
            arena = [[i for i in input().strip()] for j in range(r)]

            #print(*arena,sep='\n')

            antsInitialPositions = []
            antsDirection=[]
            antEaterPositions = []
            for i in range(r):
                for j in range(c):
                    if arena[i][j] in ['R','U','D','L']:
                        antsInitialPositions.append([i,j])
                        antsDirection.append(arena[i][j])
                    elif arena[i][j] == '#':
                        antEaterPositions.append([i,j])

            #print(antsInitialPositions)
            #print(antEaterPositions)

            antCount = len(antsInitialPositions)
            grid = [[{} for j in range(c)] for i in range(r)]

            for current in range(antCount):
                i,j = antsInitialPositions[current]
                direction = antsDirection[current]
                movei,movej = i,j
                if direction == 'D':
                    steps = 0
                    while movei<r and arena[movei][movej] != '#':
                        steps = abs(i-movei)
                        if steps in grid[movei][movej]:
                            grid[movei][movej][steps]+=1
                        else:
                            grid[movei][movej][steps]=1
                        movei+=1
                elif direction == 'U':
                    steps=0
                    while movei>=0 and arena[movei][movej] != '#':
                        steps = abs(i-movei)
                        #print("steps counted ", steps,movei,movej)
                        if steps in grid[movei][movej]:
                            #print("already there in dict")
                            grid[movei][movej][steps]+=1
                        else:
                            grid[movei][movej][steps]=1
                        movei-=1
                elif direction == 'L':
                    steps=0
                    while movej>=0 and arena[movei][movej] != '#':
                        steps = abs(j-movej)
                        if steps in grid[movei][movej]:
                            grid[movei][movej][steps]+=1
                        else:
                            grid[movei][movej][steps]=1
                        movej-=1
                elif direction == 'R':
                    steps=0
                    while movej<c and arena[movei][movej] != '#':
                        steps = abs(j-movej)
                        if steps in grid[movei][movej]:
                            grid[movei][movej][steps]+=1
                        else:
                            grid[movei][movej][steps]=1
                        movej+=1
            #print(*grid,sep='\n')
            meetings=0
            for i in range(r):
                for j in range(c):
                    for meets in grid[i][j].values():
                        if meets>=2:
                            meetings+=nCr(meets,2)
            print(int(meetings))


    except (ValueError,EOFError) as e:
        break