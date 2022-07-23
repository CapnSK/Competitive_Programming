from functools import cmp_to_key
import math

def run(debug=True):
    for _ in range(int(input())):
        n,r = list(map(int, input().split()))
        cost = list(map(int, input().split()))
        discount = list(map(int, input().split()))
        
        costEffectiveDict = {}
        for i in range(n):
            if cost[i] not in costEffectiveDict:
                costEffectiveDict[cost[i]] = discount[i]
            else:
                costEffectiveDict[cost[i]] = max(costEffectiveDict[cost[i]], discount[i])
        costEffectiveSorted = sorted(list(costEffectiveDict.items()), key = cmp_to_key(comparator))    
        if debug:
            print("cost effective dict is", costEffectiveDict)
            print("cost effective sorted dict is", costEffectiveSorted)
        
        totalItemsBought=0
        i=0
        while i<len(costEffectiveSorted):
            if costEffectiveSorted[i][0] > r:
                i+=1
                if debug:
                    print("incrementing i from first if",i)
                continue
            else:
                if debug:
                    print("numerator",r-costEffectiveSorted[i][0])
                    print("denominator",costEffectiveSorted[i][0]-costEffectiveSorted[i][1])
                itemsBoughtInThisIteration=(math.ceil((r-costEffectiveSorted[i][0])/(costEffectiveSorted[i][0]-costEffectiveSorted[i][1])))
                if itemsBoughtInThisIteration >=0:
                    remMoney=r-(itemsBoughtInThisIteration*(costEffectiveSorted[i][0]-costEffectiveSorted[i][1]))
                    if debug:
                        print("remMoney",remMoney)
                    itemsBoughtInThisIteration += 1 if remMoney>= costEffectiveSorted[i][0] else 0
                    totalItemsBought+=itemsBoughtInThisIteration
                    r-=(itemsBoughtInThisIteration*(costEffectiveSorted[i][0]-costEffectiveSorted[i][1]))
                if debug:
                    print("totalItemsBought",totalItemsBought)
                    print("itemsBoughtInThisIteration",itemsBoughtInThisIteration)
                    print("Iteration",i)
                    print("r",r)
                # itemsBought = ((r-costEffectiveSorted[i][0])//(costEffectiveSorted[i][1] or costEffectiveSorted[i][0]))+1
                # totalItemsBought+=itemsBought
                # r-=(itemsBought*(costEffectiveSorted[i][0]-costEffectiveSorted[i][1]))
                i+=1
                if debug:
                    print("incrementing i from else",i)
                continue
        if debug:
            print("totalItemsBought",totalItemsBought)
            print("i",i)
        print(totalItemsBought)
            


def comparator(item1, item2):
    if (item1[0]-item1[1])-(item2[0]-item2[1])!=0:
        return (item1[0]-item1[1])-(item2[0]-item2[1])
    else:
        return -1 if item1[0] < item2[0] else 1
  
if __name__ == '__main__':
    while True:
        try:
            run(False)
        except:
            break
