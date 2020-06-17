#include<bits/stdc++.h>
using namespace std;


vector<int> build(int l,int r,int node,vector<int> a,vector<int> st,bool debug){
    if(l==r){
        if(debug)
            cout<<"hit the base case for "<<l<<"\n";
        st[node]=a[l];
        if(debug)
            cout<<"Value of "<<node<<" after updating is "<<st[node]<<"\n";
        return st;
    }
    int mid=(l+r)/2;
    st = build(l,mid,node*2+1,a,st,debug);
    st = build(mid+1,r,node*2+2,a,st,debug);
    st[node]=min(st[2*node+1],st[2*node+2]);
    return st;
}

vector<int> update(int l,int r,int indup,int val,int node,vector<int> a,vector<int> st,bool debug){
    if(l==r){
        a[l]=val;
        st[node]=val;
        return st;
    }
    else{
        int mid=(l+r)/2;
        if(indup>=l&&indup<=mid){
            st = update(l,mid,indup,val,node*2+1,a,st,debug);
        }
        else{
            st = update(mid+1,r,indup,val,node*2+2,a,st,debug);
        }
        st[node] = min(st[2*node+1],st[2*node+2]);  
        return st;
    }
}


int query(int si,int se,int l,int r,int node,vector<int> st){
    if(se<l||si>r||l>r){
        return INT_MAX;
    }
    if(si>=l&&se<=r){
        return st[node];
    }
    int mid=(si+se)/2;
    int q1=query(si,mid,l,r,node*2+1,st);
    int q2=query(mid+1,se,l,r,node*2+2,st);
    return min(q1,q2);
}

int main(){
    bool debug = false;
    int n,q;
    cin>>n>>q;
    vector<int> arr(n);
    vector<int> st(4*n);
    
    int temp;
    for(int i=0;i<n;i++){
        cin>>temp;
        arr[i]=temp;
    }


    st = build(0,n-1,0,arr,st,debug);
    if(debug){
        for(int i=0;i<4*n;i++){
            cout<<st[i]<<" ";
        }
        cout<<endl;
    }

    int t1;
    int l,r,ind,val;
    for(int i=0;i<q;i++){
        cin>>t1;
        if(t1==1){
            cin>>l>>r;
            cout<< query(0,n-1,l-1,r-1,0,st);
        }
        else if(t1==2){
            cin>>ind>>val;
            st = update(0,n-1,ind-1,val,0,arr,st,debug);
            arr[ind] = val;
            if(debug){
                cout<<"ST after updating : ";
                for(int i=0;i<4*n;i++){
                    cout<<st[i]<<" ";
                }
                cout<<endl;
            }
        }
    }
    
    return 0;
}
