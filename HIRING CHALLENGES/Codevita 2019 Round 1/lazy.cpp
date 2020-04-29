#include <bits/stdc++.h>
using namespace std;

typedef long long int lli;

lli fact(lli num){
	lli result = 1;
	for(lli i = 2; i <= num; i++) {
		result = result * i;
	}
	return result;
}

lli nCr(lli n, lli r) {
	return (fact(n) / (fact(r) * fact(n - r)));
}


lli minv(lli a, lli m) {
	lli m0 = m;
	lli q, t;
	lli y = 0;
	lli x = 1;
	if(m == 1)
		return 0;
	while(a > 1) {
		q = a / m;
		t = m;
		m = a % m;
		a = t;
		t = y;

		y = x - q * y;
		x = t;
		if(x < 0)
			x = x + m0;
	}
	return x;
}


int main() {
	lli test;
	lli n, t, m, p, q, mod, answer;
	cin>>test;
	for(int i = 0; i < test; i++) {
		cin>>n>>t>>m;
		p = nCr(n-t, m);
		q = nCr(n, m);

		mod = 1000000007;
		answer = (q - p) * minv(q, mod) % mod;
		cout<<(int)answer<<endl;
	}
	return 0;
}