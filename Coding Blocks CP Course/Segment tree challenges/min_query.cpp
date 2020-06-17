#include<bits/stdc++.h>
using namespace std;

class segmenttree
{
public:
    int N;
    
    segmenttree(int n){
        N=n;
    }
    void build(int l,int r,int node,vector<int> a){
        if(l==r){
            st[node]=a[l];
            return;
        }
        int mid=(l+r)/2;
        build(l,mid,node*2+1,a);
        build(mid+1,r,node*2+2,a);
        st[node]=min(st[2*node+1],st[2*node+2]);
    }

    void update(int l,int r,int indup,int val,int node){
        if(l==r){
            a[l]=val;
            st[node]=val;
            return;
        }
        else{
            int mid=(l+r)/2;
            if(indup>=l&&indup<=mid){
                update(l,mid,indup,val,node*2+1);
            }
            else{
                update(mid+1,r,indup,val,node*2+2);
            }
            st[node]=min(st[2*node+1],st[2*node+2]);  
        }
    }

    int query(int si,int se,int l,int r,int node){
        if(se<l||si>r||l>r){
            return INT_MAX;
        }
        if(si>=l&&se<=r){
            return st[node];
        }
        int mid=(si+se)/2;
        int q1=query(si,mid,l,r,node*2+1);
        int q2=query(mid+1,se,l,r,node*2+2);
        return min(q1,q2);
    }
};

int main(){
    int n,q;
    cin>>n>>q;
    segmentree T=segmenttree(n);
    vector<int> arr;
    int temp;
    for(int i=0;i<n;i++){
        cin>>temp;
        arr.push_back(temp);
    }

    T.build(0,n-1,0,arr);

    for(int i=0;i<4*n;i++){
        cout<<T.st[i]<<" ";
    }
    cout<<"\n";
    return 0;
}