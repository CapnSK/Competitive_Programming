S = input().strip()

d = {}
a=[]

for ind,i in enumerate(S):
	if i in d:
		d[i]+=1
		if ind == len(S)-1:
			for key in d.keys():
				a+=[[key,d[key]]]
	else:
		if len(d)==1 :
			for key in d.keys():
					a+=[[key,d[key]]]
		d={}
		d[i]=1
		if ind == len(S)-1:
			for key in d.keys():
				a+=[[key,d[key]]]


