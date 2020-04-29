#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main(){
	int t;
	ll N,sigma,prod;
	cin >> t;
	while(t--){
		cin >> N >> sigma;
		if(N==1 && sigma == 0)
			cout << 1 << endl;
		else if(N==1)
			cout << -1 << endl;
		else{
			for (ll i = 0 ; i <= N-2 ; i++){
				cout << 0 << " ";
			}
			cout << (sigma*N)/(sqrt(N-1)) << endl;
		}
	}
}