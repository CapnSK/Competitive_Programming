from functools import cmp_to_key
import math
from pydoc import doc

def run(debug=True):
    for _ in range(int(input())):
        n=int(input())
        arr=list(map(int, input().split()))

        finalAns=0
        curr=1
        for i in range(n):
            if arr[i]==0:
                curr=1
                continue
            else:
                finalAns+=curr
                curr+=1
        print(finalAns)
  
if __name__ == '__main__':
    while True:
        try:
            run(False)
        except:
            break
