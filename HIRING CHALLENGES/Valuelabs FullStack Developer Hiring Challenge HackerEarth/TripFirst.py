import itertools
import math

def nCr(n,r):
    return math.factorial(n) // ((math.factorial(r))*(math.factorial(n-r)))


n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
    
freq = {}
freqTuple= {}
for i in a:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
        
aset = list(set(a))
combination=[]
lengthless = False
if len(aset)>=3:
    combination = list(itertools.combinations(aset,3))
    for key in combination:
        if key in freqTuple:
            freqTuple[key] +=1
        else:
            freqTuple[key] = 1
    occuredOnce = [key for key,value in freq.items() if value==1]
    occuredMultipleTimes = [key for key,value in freq.items() if value>1]
    for i in occuredOnce:
        for j in occuredMultipleTimes:
            combination.append((i,j,j))
            freqTuple[(i,j,j)]= nCr(freq[j],2)
else:
    combination = list(itertools.combinations(a,3))
    lengthless=True
answer=0
print(combination)
print(freqTuple)
for i,j,k in combination:
    Sum = i+j+k
    if (Sum%i==0 and Sum%j==0) or (Sum%j==0 and Sum%k==0) or (Sum%i==0 and Sum%k==0):
        continue
    elif Sum%i==0 or Sum%j==0 or Sum%k==0:
        if lengthless:
            answer+=6
        else:
            answer+=6*(freq[i]*freq[j]*freq[k])

print(answer)