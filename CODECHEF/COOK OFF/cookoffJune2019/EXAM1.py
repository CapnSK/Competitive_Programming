while True:
    try:
        for _ in range(int(input())):
            slen = int(input())
            correct=input().strip()
            chefAns=input().strip()
            points=0
            discard=False
            for i in range(slen):
                right = correct[i]
                answered = chefAns[i]
                if discard:
                    discard=False
                    continue
                if right == answered:
                    points+=1
                elif right != answered and answered != 'N' :
                    discard=True
                    continue
            print(points)
    except (ValueError,EOFError) as e:
        break