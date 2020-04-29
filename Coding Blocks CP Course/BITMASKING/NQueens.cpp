#include<bits/stdc++.h>
using namespace std;

int col[30],d1[30],d2[30];
int board[30][30];
void solve(int r,int n,int &ans){
	if(r==n){
		//cout<<"Base Hit\n";
		ans++;
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				cout<<board[i][j]<<" ";
			}
			cout<<endl;
		}
		cout<<"\n\n";
		return;
	}
	//cout<<"in solve\n";
	for(int c=0;c<n;c++){
		//cout<<(int)(col[c]!=0 && d1[r-c+n-1] && d2[r+c])<<endl;
		if(!col[c] && !d1[r-c+n-1] && !d2[r+c]){
			col[c]=d1[r-c+n-1]=d2[r+c]=1;
			board[r][c]=1;
			solve(r+1,n,ans);
			col[c]=d1[r-c+n-1]=d2[r+c]=0;
			board[r][c]=0;
		}
	}
}

int main(){

	int n;
	cout<<"Enter Size of chessboard"<<endl;
	cin>>n;
	int ans=0;
	solve(0,n,ans);	
	cout<<ans;
	return 0;

}