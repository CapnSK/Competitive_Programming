while True:
    try:
        for _ in range(int(input())):
            n,m = map(int,input().split())
            max_flavours = list(map(int,input().split()))
            people = []

            for i in range(n):
                people.append([i+1]+list(map(int,input().split())))

            #print(people)
            
            extra_flavors=[0 for i in range(m)]

            for person,favorite,favMoney,nonFavMoney in people:
                #print(favorite)
                extra_flavors[favorite-1]+=1
            
            #print("before",max_flavours,extra_flavors)
            remainingFlavours = []
            for i in range(m):
                extra_flavors[i] = max_flavours[i] - extra_flavors[i]
                remainingFlavours.append([i+1,extra_flavors[i]])
            #print("After",sorted(extra_flavors,reverse=True))
            _extra_flavours = sorted(remainingFlavours,reverse=True,key=lambda x:x[1])
            #print(_extra_flavours)

            profit = 0
            answer = []
            currentExtra = 0
            for person,favorite,favMoney,nonFavMoney in people:
                if max_flavours[favorite-1] > 0:
                    profit+=favMoney
                    answer.append(favorite)
                    max_flavours[favorite-1]-=1
                else:
                    profit+=nonFavMoney

                    if _extra_flavours[currentExtra][1] == 0:
                        currentExtra+=1
                        answer.append(_extra_flavours[currentExtra][0])
                        _extra_flavours[currentExtra][1]-=1
                    else:
                        answer.append(_extra_flavours[currentExtra][0])
                        _extra_flavours[currentExtra][1]-=1
            
            print(profit)
            print(*answer)



            
            
    except (ValueError,EOFError) as e:
        break