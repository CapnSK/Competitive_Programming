while True:
    try:
        for _ in range(int(input())):
            x,y,k = map(int,input().split())
            total = x+y
            playedgames = total//k
            print('Chef' if playedgames%2 == 0 else 'Paja')
    except (ValueError,EOFError) as e:
        break