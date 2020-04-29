#include <bits/stdc++.h>
using namespace std;

typedef long long int lli;

lli cal(lli i, lli j)
{
	lli temp;
	lli a,b;
	if(i==j)
		return 1;
	else{
		if(i > j){
			a = i;
			b = j;
		} else {
			a = j;
			b = i;
		}
		//cout<<a<<" "<<b<<endl;
		lli cnt=0;
		while(1){
			if(a%b==0){
				cnt+=a/b;
				break;
			}
			cnt += a/b;
			//cout<<cnt<<endl;
			temp = a;
			a = b;
			b = temp % b;
		
		}
		return cnt;
	}
}


int main()
{
	lli n,m,p,q;
	cin>>n>>m>>p>>q;
	lli answer = 0;
	for(lli i = n; i <= m; i++) {
		for(lli j = p; j <= q; j++) {
			answer += cal(i, j);
		}
	}
	cout<<answer;
	return 0;
}