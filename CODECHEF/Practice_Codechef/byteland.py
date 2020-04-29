while True :
    try :
        for _ in range(int(input())):
            n=int(input())
            t=n-1
            citizens=[1,0,0]
            bit,nibble,byte=0,1,2
            time=[2,8,16]
            i=0
            elapsedtime=0
            start=True
            while elapsedtime<=t :
                    if i == 0:
                        #print("in 0")
                        if start:
                            start=False
                            elapsedtime+=time[i]
                            i=(i+1)%3
                            continue
                        citizens[bit]=2*citizens[byte]
                        #print("multiplied by 2")
                        citizens[nibble]=0
                        citizens[byte]=0
                    elif i==1:
                        #print("in 1")
                        citizens[nibble]=citizens[bit]
                        citizens[bit]=0
                        citizens[byte]=0
                    elif i==2:
                        #print("in 2")
                        citizens[byte]=citizens[nibble]
                        citizens[bit]=0
                        citizens[nibble]=0
                    elapsedtime+=time[i]
                    i=(i+1)%3

                    #print(elapsedtime) #,i,citizens[bit],citizens[nibble],citizens[byte])
            print(*citizens)
    except (EOFError,ValueError):
        break
