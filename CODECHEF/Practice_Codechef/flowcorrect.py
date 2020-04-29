for _ in range(int(input())):
    y = int(input())
    d = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    days = (y-1900)*365
    for i in range(1900,y,4):
        if i%100!=0:
            days+=1
        elif i%400==0:
            days+=1
    print(d[days%7])