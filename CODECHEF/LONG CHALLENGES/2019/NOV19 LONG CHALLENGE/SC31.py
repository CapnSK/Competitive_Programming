def main(debug=False):
	for _ in range(int(input())):
		n=int(input())
		arr=[int(input().strip(),2) for i in range(n)]
		if debug:
			print("arr",arr)
		ans=arr[0]
		for i in range(n-1):
			if debug:
				print("ans",ans)
			ans=ans^arr[i+1]

		if debug:
			print("bin",bin(ans))
			print(list(bin(ans)))

		print(list(bin(ans)).count('1'))



while True:
	try:
		main(debug=False)
	except (ValueError,EOFError) as e:
		break