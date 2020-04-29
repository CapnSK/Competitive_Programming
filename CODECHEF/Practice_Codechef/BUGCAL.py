while True:
    try:
        for _ in range(int(input())):
            a,b = input().strip().split()
            alen,blen = len(a),len(b)
            op = []
            
            for i in range(min(alen,blen)):
                op.append(str(int(a[alen-i-1])+int(b[blen-i-1]))[-1])
            
            if alen>blen:
                rem = a[0:max(alen,blen)-min(alen,blen)]
            else:
                rem = b[0:max(alen,blen)-min(alen,blen)]
            
            print(int(rem + ''.join(op)[::-1]))

                
    except :
        break