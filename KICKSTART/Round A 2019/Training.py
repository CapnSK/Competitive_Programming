for _ in range(int(input())):
    n,p=map(int,input().split())
    skills=list(map(int,input().split()))
    sorted_skills=sorted(skills,reverse=True)
    min_hours=9999999999
    for i in range(0,n-p+1):
        extra_skills=0
        for j in range(i+1,i+p):
            extra_skills+=(sorted_skills[i]-sorted_skills[j])
        #print(i,j,extra_skills)
        if extra_skills<min_hours and extra_skills>=0:
            min_hours=extra_skills
            
    print("Case #",_+1,":",sep="",end=" ")
    print(min_hours)