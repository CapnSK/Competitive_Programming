#include<bits/stdc++.h>
using namespace std;
int main(){
	int t,n,k;
	cin >> t;
	while(t--){
		int cnt = 0;
		cin >> n >> k;
		int arr[n];
		for(int i = 0 ; i < n ; i ++){
			cin >> arr[i];
			if(arr[i]>k){
				cnt +=1;
			}
		}
		sort(arr,arr+n);
		int i = n-cnt;
		int j = n - 1;

		while(cnt>=2){
			cout << i << " " << j << endl;
			int diff = arr[i]-k;
			cout << diff << " " << endl;
			arr[i]-=diff;
			arr[j] -= diff;
			cnt -=1;
			i+=1;
			if(arr[j]<=k)
				j-=1;
		}
		unsigned long long sum = 0;
		for(int i = 0 ; i < n ; i++){
			cout << arr[i] << " ";
			sum+=arr[i];
		}
		cout << "\n";
		cout << sum << "\n";

	}
}