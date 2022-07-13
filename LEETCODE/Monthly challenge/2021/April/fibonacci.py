def main(debug = False):
    n = int(input())
    if n<2:
        if n==0:
            print(0)
        elif n==1:
            print(1)
    else:
        prev, curr = 0,1
        i=1
        while i<n:
            if debug:
                print("i ans",i,curr)
            temp = curr
            curr += prev
            prev = temp
            i+=1
        print(curr)
main(debug=False)