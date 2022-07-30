from functools import cmp_to_key
import math
from pydoc import doc

def run(debug=True):
    for _ in range(int(input())):
        n=int(input())
        arr=list(map(int, input().split()))
        sortedArr = sorted(arr)

        rem=[]
        curr=0
        for i in range(n):
            if arr[i]==sortedArr[curr]:
                curr+=1
                continue
            else:
                rem.append(arr[i])
        
        remSorted=sorted(rem)
        poss=True
        for i in range(len(rem)):
            if rem[i]!=remSorted[i]:
                poss=False
                break
        print("YES" if poss else "NO")

  
if __name__ == '__main__':
    while True:
        try:
            run(False)
        except:
            break
