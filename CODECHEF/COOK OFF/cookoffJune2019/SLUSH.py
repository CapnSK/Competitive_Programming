while True:
    try:
        for _ in range(int(input())):
            n,m = map(int,input().split())
            max_flavours = list(map(int,input().split()))
            people = []

            for i in range(n):
                people.append([i+1]+list(map(int,input().split())))

            print(people)
            
            extra_flavors=[0 for i in range(m)]

            for person,favorite,favMoney,nonFavMoney in people:
                print(favorite)
                extra_flavors[favorite-1]+=1
            
            #print("before",max_flavours,extra_flavors)

            for i in range(m):
                extra_flavors[i] = max_flavours[i] - extra_flavors[i]

            #print("After",sorted(extra_flavors,reverse=True))

            
            
    except (ValueError,EOFError) as e:
        raise e