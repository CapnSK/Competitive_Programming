def main(debug=False):
    s1=input()  
    s2=input()
    i,j=0,0
    l=[]
    try:
        i=s1.index(s2[0])
        j=i+1
        k=1
        while i<len(s1):
            if debug:
                print("for i=",i)
            while j<len(s1):
                if debug:
                    print("for j=",j)
                if k==len(s2)-1:
                    if debug:
                        print("k is",k)
                    l.append(s1[i:j+1:])
                    break
                k+=1
                j=s1.index(s2[k],j+1)
            i=s1.index(s2[0],i+1)
            j=i+1
            k=1
    
    except ValueError:
        print(min(l))

main(debug=False)