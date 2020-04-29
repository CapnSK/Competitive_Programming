while True:
	try :
		for _ in range(int(input())):
			n=int(input())
			recipes=[]
			sets=[]
			for i in range(n):
				temp=input().strip()
				recipes.append(temp)
				sets.append(sorted(list(set(list(temp)))))
			cnt = [0 for i in range(26)]

			for recipe in sets:
				for ing in recipe:
					cnt[ord(ing)-97]+=1
			print(cnt.count(n))
			
	except : 
		break