def possible(minutes,painters,n,boards):
	paintersUsed=1
	cnt=0
	i,j,current=0,0,0
	while i<n:
		if boards[i]>minutes:
			return False

		if current + boards[i]>mid:
			current=0
			j+=1
		current+=boards[i]

		i+=1
	j+=1
	return j<=painters

def getAns(k,n,painters):
	s=painters[0]
	e=sum(painters)
	ans=-1

	while s<=e:
		mid = (s+e)//2
		poss = possible(mid,k,n,painters)
		if poss:
			e=mid-1
			ans=mid
		else:
			s=mid+1
	return ans
def main(debug=False):
	k,n=int(input()),int(input())
	painters=list(map(int,input().split()))
	print(getAns(k,n,sorted(painters)))

main(debug=False)



'''
bool is_valid(int mid){
	int i = 0, j = 0,current = 0;
	while(i < n){
		if(boards[i] > mid)
			return false;

		//cout << current + boards[i] << endl;
		if(current + boards[i] > mid){
			//cout << "i is " << i << endl;
			current = 0;
			j++;
		}
		current += boards[i];
		i++;
	}
	j++;
	//cout << j << " " << mid << endl;
	return (j <= painters);
}

void executor(int test_case){
	cin >> painters >> n;
	getarr(boards,n);
	//sort(boards,boards+n,greater<int>());
	int s = boards[0];
	int e = accumulate(boards,boards+n,0);
	int ans = -1;
	while(s <= e){
		int mid = (s+e)/2;
		if(is_valid(mid)){
			ans = mid;
			e = mid - 1;
		}else{
			s = mid + 1;
		}
	}
	cout << ans << endl;
}

'''