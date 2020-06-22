def main(debug=False):
	for _ in range(int(input())):
		ts = int(input())
		if ts&1:
			print(ts//2)
		else:
			binTs = bin(ts)[2::]
			i=len(binTs)-1
			cnt=0
			while binTs[i]!='1':
				cnt+=1
				i-=1
			cnt+=1
			ans=1<<cnt
			if debug:
				print("1st set bit at position",cnt)
				print("ans",ans)

			ans = ts//ans
			print(ans)


while True:
	try:
		main(debug=False)
	except (ValueError,EOFError) as e:
		break