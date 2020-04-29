Dynamic = {}

def squares(w,h):
	# if w == 1 and h == 1:
	# 	return 1
	# elif w == h:
	# 	return 1
	# elif w > h:
	# 	return 1 + squares(w-h,h)
	# elif h > w:
	# 	return 1 + squares(w,h-w)
	if (w,h) in Dynamic:
		return Dynamic[(w,h)]
	elif (h,w) in Dynamic:
		return Dynamic[(w,h)]
	Total = 0
	width = w
	height = h
	while w != h:
		if w > h:
			w = w - h
			Total +=1
		elif w < h:
			h = h - w
			Total +=1

	Dynamic[(width,height)] = Total + 1
	Dynamic[(height,width)] = Total + 1
	return Total + 1


MinLength = int(input())
MaxLength = int(input())
MinWidth = int(input())
MaxWidth = int(input())

# print(squares(6,3))
Total = 0
for length in range(MinLength,MaxLength+1):
	for width in range(MinWidth,MaxWidth+1):
		#print(length,width,squares(width,length))
		Total += squares(length,width)
print(Total)