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
        

combination=[]
aset = list(set(a))
if len(aset)>=3:
    combination = list(itertools.combinations(aset,3))
    #print(combination)
    for i,j,k in combination:
            freqTuple[(i,j,k)] = 1*freq[i]*freq[j]*freq[k]

    l = list(freq.keys())
    llen = len(l)
    for i in range(llen):
        for j in range(llen):
            i1,j1 = min(l[i],l[j]),max(l[i],l[j])
            if i1!=j1:
                if freq[j1]>1 and freq[i1]==1:
                    combination.append((i1,j1,j1))
                    freqTuple[(i1,j1,j1)] = nCr(freq[j1],2)
                if freq[i1]>1 and freq[j1]==1:
                    combination.append((i1,i1,j1))
                    freqTuple[(i1,i1,j1)] = nCr(freq[i1],2)
                if freq[i1]>1 and freq[j1]>1:
                    #print("IN here")
                    combination.append((i1,j1,j1))
                    freqTuple[(i1,j1,j1)] = freq[i1]*nCr(freq[j1],2)
                    combination.append((i1,i1,j1))
                    freqTuple[(i1,i1,j1)] = freq[j1]*nCr(freq[i1],2)


else:
    i,j = map(int,freq.keys())
    i,j = min(i,j),max(i,j)
    if freq[j]>1 and freq[i]==1:
        combination.append((i,j,j))
        freqTuple[(i,j,j)] = nCr(freq[j],2)
    if freq[i]>1 and freq[j]==1:
        combination.append((i,i,j))
        freqTuple[(i,i,j)] = nCr(freq[i],2)
    if freq[i]>1 and freq[j]>1:
        #print("IN here")
        combination.append((i,j,j))
        freqTuple[(i,j,j)] = freq[i]*nCr(freq[j],2)
        combination.append((i,i,j))
        freqTuple[(i,i,j)] = freq[j]*nCr(freq[i],2)



answer=0
#print(combination)
#print(freqTuple)
for i,j,k in freqTuple.keys():
    Sum = i+j+k
    if (Sum%i==0 and Sum%j==0) or (Sum%j==0 and Sum%k==0) or (Sum%i==0 and Sum%k==0):
        continue
    elif Sum%i==0 or Sum%j==0 or Sum%k==0:
        answer+=6*freqTuple[(i,j,k)]

print(answer)