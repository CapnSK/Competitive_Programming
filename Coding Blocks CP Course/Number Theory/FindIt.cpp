#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
vector<int> sum(100001);
void precompute(vector<int> arr){
	//cout<<"In precompute\n";
	vector<int> cnt(100001);
	fill(cnt.begin(),cnt.end(),0);
	for(int i=0;i<arr.size();i++){
		cnt[arr[i]]+=1;
	}
	//cout<<"After first for loop \n";
	for(int i=2;i<sum.size();i++){
		for(int j=i;j<cnt.size();j+=i) sum[i]+=cnt[j];
	}
	//cout<<"Completed the execution\n";
	return;
}

int main() {
	
	int n,q;
	cin>>n;
	vector<int> arr(n);
	for(int i=0;i<n;i++) cin>>arr[i];
	precompute(arr);
	cin>>q;
	int qi;
	while(q--){
		cin>>qi;
		cout<<sum[qi]<<"\n";
	} 

	return 0;
}