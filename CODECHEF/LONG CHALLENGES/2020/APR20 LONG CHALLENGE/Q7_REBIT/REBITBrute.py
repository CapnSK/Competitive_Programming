from itertools import *
from copy import deepcopy
for _ in range(int(input())):
	l=list(input().strip())
	poss={'0':{'0':{'^':1,'&':4,'|':1},'1':{'^':1,'&':0,'|':1},'a':{'^':1,'&':0,'|':1},'A':{'^':1,'&':0,'|':1}},  '1':{'0':{'^':1,'&':1,'|':0},'1':{'^':1,'&':1,'|':4},'a':{'^':1,'&':1,'|':0},'A':{'^':1,'&':1,'|':0}},  'a':{'0':{'^':1,'&':2,'|':0},'1':{'^':1,'&':0,'|':2},'a':{'^':1,'&':2,'|':2},'A':{'^':1,'&':0,'|':0}},  'A':{'0':{'^':1,'&':2,'|':0},'1':{'^':1,'&':0,'|':2},'a':{'^':1,'&':0,'|':0},'A':{'^':1,'&':2,'|':2}}}
	inds=[]
	
	for i in range(len(l)):
		if l[i]=='#':
			inds.append(i)

	all_combs=list(product(poss,repeat=len(inds)))

	for combs in all_combs:
		tmp=deepcopy(l)
		for j in range(len(inds)):
			tmp[inds[j]]=combs[j]
		print(''.join(tmp))