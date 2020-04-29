#include<bits/stdc++.h>
using namespace std;
void go(string s,int open,int close,int pos,int n){
	//cout<<pos<<" ";
	if(pos==(2*n)){
		//cout<<"o c "<<open<<close<<endl;
		//cout<<s<<endl;
		if(open==close){
			cout<<s<<endl;
		}
		return;
	}
	if(open>close){
		go(s+")",open,close+1,pos+1,n);
	}
	if(open<n){
		go(s+"(",open+1,close,pos+1,n);
	}
	return;
}
void printAllCombinations(int n){
	go("(",1,0,1,n);
}
int main() {
	int n;
	cin>>n;
	printAllCombinations(n);
	return 0;
}