#include <bits/stdc++.h>
using namespace std;

class Node{
    public:
        char data;
        map<char,Node*> children;
        bool terminal;

        Node(char d){
            data = d;
            terminal = false;
        }
};

class Trie{
    Node* root;
    int cnt;

    public:

    Trie(){
        root = new Node('\0');
        cnt = 0;
    }

    void insert(char *w){

        Node* temp = root;
        for(int i=0;w[i]!='\0';i++){

            char ch = w[i];
            if(temp->children.count(ch)){
                temp = temp->children[ch];
            }
            else{
                Node* n = new Node(ch);
                temp->children[ch] = n;
                temp = n;
            }
        }
        temp->terminal = true;
    }

    bool find(char *w){
        Node* temp = root;
        for(int i=0;w[i]!='\0';i++){
            char ch = w[i];
            if(temp->children.count(ch)==0){
                return false;
            }
            else{
                temp = temp->children[ch];
            }
        }
        return temp->terminal;
    }
};

int main(){
	int n;
	cout<<"Enter Number of words to inser in Dict:\n";
	cin>>n;
	char word[100];
	cout<<"Enter words to enter\n";
	Trie dict;
	for(int i=0;i<n;i++){
		cin>>word;
		dict.insert(word);
	}


	cout<<"Enter number of words to search\n";
	int q; cin>>q;
	bool present;
	for(int i=0;i<q;i++){
		cin>>word;
		present = dict.find(word);
		if(present) cout<<"Word present\n";
		else cout<<"Word absent\n";
	}
    
}