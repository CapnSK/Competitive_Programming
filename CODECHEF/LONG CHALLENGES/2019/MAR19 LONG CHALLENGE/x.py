			'''
			all_combs=sorted(all_combs,key=lambda x:len(x))
			print(all_combs)

			final=0

			for a in all_combs:
				l,r=a[0],a[-1]
				m=int(math.ceil(k/(r-l+1)))
				a=a*m
				a=sorted(a)
				x=a[k-1]
				count=a.count(x)
				if count in a:
					final+=1

			print(final)

			'''