while True :
	try :
		for _ in range(int(input())):
			n=int(input())
			#dishes=[]
			dishes={}

			aeiou=0

			for i in range(n):
				temp=list(set(list(input())))
				temp=''.join(sorted(temp))
				ingredients=[]

				have_vowel=False
				only_consonants=0
				


				for i in temp:
					if i in ['a','e','i','o','u']:
						ingredients.append(i)
						have_vowel=True

				if not have_vowel:
					only_consonants+=1
					ingredients='z'

				ingredients=''.join(ingredients)
				if ingredients=='aeiou':
					aeiou+=1



				#print(ingredients)
				if ingredients in dishes :
					dishes[ingredients]+=1
				else:
					dishes[ingredients]=1



				#dishes.append(temp)

			dishes=dict(sorted(dishes.items()))
			count=0
			#print(aeiou)
			if aeiou>1:
				count=(aeiou*(aeiou-1))//2
			if only_consonants>0 and aeiou > 1 :
				count+=dishes['aeiou']*dishes['z']
				del dishes['z']
			dishes=sorted(dishes.items())
			length=len(dishes)

			#print(dishes,length)
			#print("before",count)
			for j in range(0,length,1):
				for i in range(j,length,1):
					temp=''.join(sorted(list(set(list(dishes[i][0]+dishes[j][0])))))
					if temp=='aeiou' and i!=j:
						
						count+=dishes[i][1]*dishes[j][1]
						#print(temp,dishes[i][0],dishes[j][0],count)
			
			print(count)
			
	except :
		break