#include<bits/stdc++.h>
using namespace std;
int main(){
	int t,n,k;
	cin >> t;
	while(t--){
		int cnt = 0;
		k = 50000;
		n = 50;
		int arr[n];
		for(int i = 0 ; i < n ; i ++){
			arr[i] = 50000;
			if(arr[i]>k){
				cnt +=1;
			}
		}
		sort(arr,arr+n);
		int i = n-cnt;
		int j = n - cnt + 1;

		while(cnt>=2){
			cout << i << " " << j << endl;
			int diff = arr[i]-k;
			cout << diff << " " << endl;
			arr[i]-=diff;
			arr[j] -= diff;
			cnt -=1;
			i+=1;
			j+=1;
		}
		long sum = 0;
		for(int i = 0 ; i < n ; i++){
			sum+=arr[i];
		}
		cout << sum << "\n";

	}
}