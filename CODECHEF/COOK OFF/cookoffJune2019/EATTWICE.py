while True:
    try:
        for _ in range(int(input())):
            n,m = map(int,input().split())
            wt = [] 
            val =[]
            week={}
            for i in range(n):
                d,v=list(map(int,input().split()))
                wt.append(d)
                val.append(v)
                if d in week:
                    if(week[d]<v):
                        week[d]=v
                else:
                    week[d]=v

                
            print(sum(sorted(week.values(),reverse=True)[:2:]))
            #print(week)

    except (ValueError,EOFError) as e:
        break