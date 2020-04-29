#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
ll Max=1000000000;
vector<ll> primesTillRtN;
void Sieve(){
	vector<ll> p;
	for(int i=0;i*i<=Max;i++) p.push_back(true);
	p[0]=p[1]=false;
	for(int i=4;i<p.size();i+=2) p[i]=false;
	for(int i=3;i<p.size();i++){
		if(p[i]){
			for(int j=i*i;j<p.size();j+=i) p[j]=false;
		}
	}
	for(ll i=0;i<p.size();i++)
		if(p[i])
			primesTillRtN.push_back(i);
}
vector<ll> SegmentedSieve(ll a,ll b){
	vector<ll> arr;
	vector<bool> tmp;
	for(ll i=0;i<= b-a ;i++) tmp.push_back(true);

	for(int k=0;k<primesTillRtN.size();k++){
		ll i=primesTillRtN[k];
		//cout<<" i "<<i<<" ";
		if(i*i >b) break;
		int rem=a%i;

		int startInd=a;
		if(rem!=0)startInd+=(i-rem); 
		//cout<<"for i "<<i<<" StartIndex is "<<startInd<<" \n";
		int j=startInd;
		while(j<=b){
			if(j==i){
				j+=i;
				continue;
			}
			tmp[j-a]=false;
			j+=i;
		}
	}

	if(a==1) tmp[0]=false;
	for(ll i=0;i<tmp.size();i++){
		if(tmp[i]){
			arr.push_back(a+i);
		}
	}
	return arr;
}
int main() {
	ll m,n;
	ll t;
	cin>>t;
	Sieve();
	while(t--){
	cin>>m>>n;
	vector<ll> ans=SegmentedSieve(m,n);
	for(ll i=0;i<ans.size();i++) cout<<ans[i]<<"\n";
	cout<<"\n";
	}
	return 0;
}