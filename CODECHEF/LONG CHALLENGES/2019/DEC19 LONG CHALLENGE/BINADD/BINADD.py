def main(debug=False):
	for _ in range(int(input())):
		a=int(input(),2)
		b=int(input(),2)
		cnt=0
		while b!=0:
			u=a^b
			v=a&b
			a=u
			b=v<<1
			cnt+=1
		print(cnt)
while True:
	try:
		main(debug=False)
	except (ValueError,EOFError) as e:
		break