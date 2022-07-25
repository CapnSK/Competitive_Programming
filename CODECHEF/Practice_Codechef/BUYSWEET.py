from functools import cmp_to_key
import math
from pydoc import doc

def run(debug=True):
    for _ in range(int(input())):
        n,r = list(map(int, input().split()))
        cost = list(map(int, input().split()))
        discount = list(map(int, input().split()))
        discountedCost = []
        for i in range(n):
            discountedCost.append([cost[i]-discount[i] ,i])
        discountedCost.sort(key=lambda x:x[0])
        ans=0
        for i in range(n):
            [currDiscountedCost, ind] = discountedCost[i]
            currCost = cost[ind]
            currDiscount = discount[ind]
            if currCost>r:
                continue
            bought=((r-currDiscount)//(currDiscountedCost))
            ans+= bought
            r-=bought*currDiscountedCost
        print(ans)
  
if __name__ == '__main__':
    while True:
        try:
            run(False)
        except:
            break
