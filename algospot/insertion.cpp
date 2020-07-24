#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

typedef int Keytype;

struct Node
{
	Keytype key;
	int priority,size;
	Node *left,*right;
	Node(const Keytype& _key):key(_key),priority(rand()),size(1),left(NULL),right(NULL)
	{}
	void setleft(Node* newleft){left=newleft;calcSize();}
	void setright(Node* newright){right=newright;calcSize();}
	void calcSize()
	{
		size=1;
		if(left)size+=left->size;
		if(right)size+=right->size;
	}
};

typedef pair<Node*,Node*> Nodepair;

Nodepair split(Node* root,Keytype key)
{
	if(root==NULL)return Nodepair(NULL,NULL);
	if(root->key<key)
	{
		Nodepair rs=split(root->right,key);
		root->setright(rs.first);
		return Nodepair(root,rs.second);
	}
	Nodepair ls=split(root->left,key);
	root->setleft(ls.second);
	return Nodepair(ls.first,root);
}

Node* insert(Node* root,Node* node)
{
	if(root==NULL) return node;
	if(root->priority<node->priority)
	{
		Nodepair splitted=split(root,node->key);
		node->setleft(splitted.first);
		node->setright(splitted.second);
		return node;
	}
	else if(node->key<root->key)
		root->setleft(insert(root->left,node));
	else
		root->setright(insert(root->right,node));
	return root;
}

Node* merge(Node* a,Node* b)
{
	if(a==NULL) return b;
	if(b==NULL) return a;
	if(a->priority<b->priority)
	{
		b->setleft(merge(a,b->left));
		return b;
	}
	a->setright(merge(a->right,b));
	return a;
}

Node* erase(Node* root,Keytype key)
{
	if(root==NULL) return root;
	if(root->key==key)
	{
		Node* ret=merge(root->left,root->right);
		delete root;
		return ret;
	}
	if(key<root->key)
		root->setleft(erase(root->left,key));
	else
		root->setright(erase(root->right,key));
	return root;
}

Node* kth(Node* root,int k)
{
	int leftsize=0;
	if(root->left!=NULL)leftsize=root->left->size;
	if(k<=leftsize)return kth(root->left,k);
	if(k==leftsize+1)return root;
	return kth(root->right,k-leftsize-1);
}

int countlessthan(Node* root,Keytype key)
{
	if(root==NULL) return 0;
	if(root->key>=key)
		return countlessthan(root->left,key);
	int ls=(root->left?root->left->size:0);
	return ls+1+countlessthan(root->right,key);
}

int n,shifted[50000],a[50000];

void solve()
{
	Node* candidates=NULL;
	for(int i=0;i<n;i++)
		candidates=insert(candidates,new Node(i+1));
	for(int i=n-1;i>=0;i--)
	{
		int larger=shifted[i];
		Node* k=kth(candidates,i+1-larger);
		a[i]=k->key;
		candidates=erase(candidates,k->key);
	}
}

int main()
{
	int t,i;
	cin>>t;
	while(t--)
	{
		cin>>n;
		for(i=0;i<n;i++)
			cin>>shifted[i];
		solve();
		for(i=0;i<n;i++)
			cout<<a[i]<<" ";
		cout<<endl;
	}
	return 0;
}