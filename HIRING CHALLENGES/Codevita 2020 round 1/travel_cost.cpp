#include<bits/stdc++.h>
using namespace std;

int main(){
	int n;
	cin>>n;
	bool debug = false;
	vector<int> arr(n);
	vector<int> dp(n);
	int k;

	for(int i=0;i<n;i++) cin>>arr[i];
	
	cin>>k;

	for(int i=0;i<n;i++) dp[i] = INT_MAX;

	dp[0] = arr[0];
	
	if(arr[n-1] == -1){ cout<<-1; exit(0);}

	if(debug){
			//cout<<endl<<"dp before: ";
			cout<<INT_MAX<<endl;
			for(int i=0;i<n;i++){
				cout<<dp[i]<<" ";
			}
			cout<<"\n";
		}
	int prev;
	for(int i=1;i<n;i++){
		if(arr[i]==-1) continue;
		for(int j=0;j<=k;j++){
			if(i-j < 0) break;
			if(debug) cout<<i<<" "<<j<<"\n";
			prev = i-j-1;
			if(arr[prev]!=-1){
				dp[i] = min(dp[prev]+arr[i],dp[i]);
				//cout<<dp[i]<<" ";
			}

		}
		if(debug){
			cout<<endl<<"\t";
			for(int i=0;i<n;i++){
				cout<<dp[i]<<" ";
			}
			cout<<"\n";
		}
		//cout<<endl<<dp[i]<<" ";
	}
	if(dp[n-1] == INT_MAX)
		cout<<-1<<"\n";
	else
		cout<<dp[n-1]<<"\n";

	return 0;
}