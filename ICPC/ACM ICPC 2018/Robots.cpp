#include<bits/stdc++.h>
using namespace std;
int max(int a,int b){
	return a > b?a:b;
}
int min(int a,int b){
	return a < b ? a:b;
}
int main(){
	int t;
	string s;
	cin >> t;
	while(t--){
		int flag = 0;
		cin >> s;
		int len = s.length();
		int a[len] = {0};

		for(int i = 0 ; i < len;i++){
			if (s[i]=='.')
				continue;
			else{
				int val = s[i]-48;
				for(int j = max(0,i-val) ; j <= min(len,val+i) ; j++){
					a[j] += 1;
				}
			}
		}
		for(int i = 0 ; i < len;i++){
			if (a[i]>1){
				flag = 1;
				break;
			}
		}
		if(flag)
			cout <<"unsafe"<<"\n";
		else
			cout<<"safe" << "\n";
	}
}