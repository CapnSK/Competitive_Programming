#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
vector<ll> divisors(1000001);
void precompute(){
	fill(divisors.begin(),divisors.end(),-1);
	divisors[1]=1;
	for(int i=2;i<divisors.size();i+=2) divisors[i]=2;

	for(int i=3;i<divisors.size();i+=2){
		if(divisors[i]==-1){
			divisors[i]=i;
			for(int j=i*i;j<divisors.size();j+=i){
				if(divisors[j]==-1) divisors[j]=i;
			}
		}
	}

	// for(int i=0;i<30;i++) cout<<divisors[i]<<" ";
	// cout<<endl;
}
ll MOD=1000000007;
ll calcPrimeFactors(vector<ll> arr){
	ll divs=1;
	map<ll,ll> Dict;
	ll n;
	for(int i=0;i<arr.size();i++){
		n=arr[i];
		while(n>1){
			//cout<<n<<" ";
			if(Dict.count(divisors[n])==0){
				Dict[divisors[n]]=0;
			}
			Dict[divisors[n]]+=1;
			n=(n/divisors[n]);
		}
	}
	for(map<ll,ll>::iterator it=Dict.begin();it!=Dict.end();it++){
		//cout<< it->first<<" "<<it->second<<"\n";
		divs = ((divs%MOD)*((it->second +1)%MOD))%MOD;
	}
	return divs%MOD;
}
int main() {
	ll n,t;
	precompute();
	cin>>t;
	ll temp;
	while(t--){
		cin>>n;
		vector<ll> v(n);
		for(int i=0;i<n;i++) cin>>v[i];
		cout<<calcPrimeFactors(v)<<"\n";
	}
	return 0;
}