def search(key,arr,s,i,e):

	while s<=e:
		mid=(s+e)//2
		if arr[mid]==key and i!=mid:
			return True
		elif arr[mid]>key:
			e=mid-1
		else:
			s=mid+1
	return False

def getAns(prices,n,money,debug):
	final_ans=[]
	for i in range(n): # in prices:
		price1=prices[i]
		price2= money - price1
		if search(price2,prices,0,i,n-1):
			if len(final_ans)==0 or abs(price1-price2)<abs(final_ans[0]-final_ans[1]):
				final_ans=[]
				final_ans.append(min(price1,price2))
				final_ans.append(max(price1,price2))
	return final_ans

def main(debug=False):
	output=[]
	for _ in range(int(input())):
		n=int(input())
		prices=sorted(list(map(int,input().split())))
		money=int(input())
		input()
		output.append(getAns(sorted(prices),n,money,debug))
	for i in output:
		print("Deepak should buy roses whose prices are {0} and {1}.".format(i[0],i[1]))

main(debug=False)