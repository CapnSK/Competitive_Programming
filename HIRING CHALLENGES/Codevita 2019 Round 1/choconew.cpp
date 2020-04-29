#include<bits/stdc++.h>
using namespace std;

#define ll long long 
#define db double
#define ldb long double 
#define pii pair<int,int>
#define pll pair<long long,long long>
#define mk(x,y) make_pair(x,y)
#define vi vector<int>
#define vll vector<long long>
#define vpii vector<pair<int,int> > 
#define vpll vector<pair<long long,long long> >
#define pb(x) push_back(x)
#define fir first
#define sec second
#define all(x) x.begin(),x.end()
#define FILE freopen("input.txt", "rt", stdin),freopen("output.txt", "wt", stdout);
#define IOS ios_base::sync_with_stdio(0);
#define mod 1000000007

ll expo(ll base,ll exp){
	ll ans=1;
	while(exp){
		if(exp%2) ans=(ans%base)%mod;
		exp/=2;
		base=(base*base)%mod;
	} return ans;
}

ll dp[1001][1001],sum[1001][1001];

ll solve(ll n,ll m){
	if(n==1 || m==1)
		return m*n;
	if(dp[n][m]!=-1)
		return dp[n][m];

	if(n==m)
		dp[n][m]=1;
	else if(n<m)
		dp[n][m]=1+solve(n,m-n);
	else
		dp[n][m]=1+solve(n-m,m);

	return dp[n][m];
}

void pre(){
    for(int i=1;i<=1000;i++){
		for(int j=1;j<=1000;j++){
			dp[i][j]=-1;
			sum[i][j]=0;
		}
	}
	for(int i=1;i<=1000;i++){
		for(int j=1;j<=1000;j++){
			sum[i][j]=sum[i][j-1]+solve(i,j);
        }
	}
}

ll sol(ll n,ll m){
    ll ans,j,k;
    k=n/m;
    j=n%m;
    ans = m*k*(k-1)/2 + k*sum[m][m] + k*j + sum[m][j];
    return ans;
}

int main(){
	IOS
    pre();
    int t;
    cin>>t;
    while(t--){
        ll i,n,m,p,q,ans=0;
        cin>>m>>n>>p>>q;
        
        for(i=p;i<=q;i++){
            ans+=(sol(n,i)-sol(m-1,i));
        }
        
        printf("%lld\n",ans);
    }
}