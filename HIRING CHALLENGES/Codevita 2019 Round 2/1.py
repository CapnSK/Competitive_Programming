def dist(i,j,h,k):
	return abs(i-h + j-k)+abs(i-h -j+k)

while True:
	try:
		n=int(input())
		arr=[]
		d={}
		h,k=n//2,n//2
		for i in range(n):
			tmp=''.join(input().split())
			#print(tmp)
			arr.append(tmp)
			for j in range(n):
				if tmp[j]=='X':
					r=dist(i,j,h,k)
					d[r]=(i,j)

		d=sorted(list(d.items()),key=lambda x:x[0],reverse=True)
		strip={}
		c=0
		for ke,v in d:
			strip[ke]=c
			c+=1

		dist1=0
		c=0
		rots={}
		count=0
		for ke,v in d:
			cc,ccc=0,0
			dist1= abs(v[0]-c)+abs(v[1]-c)
			y1,x1=v[0],v[1]
			if y1==c+ke and x1!=c+ke:
				ccc=1
			elif x1==c and y1!=c:
				ccc=1
			elif y1==c and x1!=c:
				cc=1
			elif x1==c+ke and y1!=c+ke:
				cc=1
			elif x1==c+ke and y1==c+ke:
				cc=1
			c+=1

			#print(cc,ccc,dist1)
			
			if cc==1:
				print(dist1,end="")
				rots[ke]=dist1
			elif ccc==1:
				print(-dist1,end="")
				rots[ke]=-dist1

			if count==len(d)-1:
				break
			print(end=" ")
			count+=1

		print()
		new=[["0" for i in range(n)] for j in range(n)]
		new[n//2][n//2]=arr[n//2][n//2]
		c=1
		layer=0

		for i in range(n):
			for j in range(n):
				if i==h and j==k:
					continue
				r=dist(i,j,h,k)
				s=strip[r]
				dis=rots[r]
				old=arr[i][j]


				Is,js,isr,jsr=False,False,False,False

				if i==s+r and j==s+r:
					if dis>0:
						jsr=True
					else:
						isr=True

				elif i==s and j==s:
					if dis>0:
						js=True
					else:
						Is=True

				elif j==s and i==s+r:
					if dis>0:
						isr=True
					else:
						js=True
				elif j==s+r and i==s:
					if dis>0:
						Is=True
					else:
						jsr=True
				elif j==s+r:
					jsr=True
				elif j==s:
					js=True
				elif i==s+r:
					isr=True
				elif i==s:
					Is=True


				if jsr:
					if dis>0:
						if i-dis>=s:
							new[i-dis][j]=old
						else:
							done=i-s
							dis=dis-done
							new[s][j-dis]=old
					elif dis<0:
						dis=abs(dis)
						if i+dis<=s+r:
							new[i+dis][j]=old
						else:
							done=s+r-i
							dis=dis-done
							new[s+r][j-dis]=old

				elif isr:
					if dis>0:
						if j+dis<=s+r:
							new[i][j+dis]=old
						else:
							done=s+r -j
							dis=dis-done
							new[i-dis][s+r]=old
					elif dis<0:
						dis=abs(dis)
						if j-dis>=s:
							new[i][j-dis]=old
						else:
							done=j-s
							dis=dis-done
							new[i-dis][s]=old

				elif js:
					if dis>0:
						if i+dis<=s+r:
							new[i+dis][j]=old
						else:
							done = s+r -i
							dis=dis-done
							new[s+r][j+dis]=old
					elif dis<0:
						dis=abs(dis)
						if i-dis>=s:
							new[i-dis][j]=old
						else:
							done=i-s
							dis=dis-done
							new[s][j+dis]=old


				elif Is:
					if dis>0:
						if j-dis>=s:
							new[i][j-dis]=old
						else:
							done=j-s
							dis=dis-done
							new[i+dis][s]=old
					elif dis<0:
						dis=abs(dis)
						if j+dis<=s+r:
							new[i][j+dis]=old
						else:
							done= s+r -j
							dis = dis-done
							new[i+dis][s+r]=old

		for i in range(n):
			print(*new[i],end="")
			if i==n-1:
				break
			print()


	except (ValueError,EOFError) as e:
		break