#include <string>
#include <vector>
#include <algorithm>

using namespace std;
struct node
{
    int x;
    int y;
    int num;
};

struct tree
{
    node no;
    tree *l;
    tree *r;
};

vector<int> ans1,ans2;

bool cmp(node a,node b)
{
    if(a.y==b.y)return a.x<b.x;
    else return a.y>b.y;
}

void add_node(tree *root,tree *tmp)
{
    if(tmp->no.x<root->no.x)
    {
        if(root->l!=NULL)add_node(root->l,tmp);
        else root->l=tmp;
    }
    else
    {
        if(root->r!=NULL)add_node(root->r,tmp);
        else root->r=tmp;
    }
}
void pre(tree *root)
{
    if(root!=NULL)
    {
        ans1.push_back(root->no.num);
        pre(root->l);
        pre(root->r);
    }
}
void post(tree *root)
{
    if(root!=NULL)
    {
        post(root->l);
        post(root->r);
        ans2.push_back(root->no.num);
    }
}

vector<vector<int>> solution(vector<vector<int>> nodeinfo)
{
    vector<vector<int>> answer;
    vector<node> n;

    for(int i=0;i<nodeinfo.size();i++)
    {
        node tmp;
        tmp.x=nodeinfo[i][0];
        tmp.y=nodeinfo[i][1];
        tmp.num=i+1;
        n.push_back(tmp);
    }

    stable_sort(n.begin(),n.end(),cmp);

    tree *root=new tree;
    root->no=n[0];
    root->l=NULL;
    root->r=NULL;

    for(int i=1;i<n.size();i++)
    {
        tree *tmp=new tree;
        tmp->no=n[i];
        tmp->l=NULL;
        tmp->r=NULL;
        add_node(root,tmp);
    }

    pre(root);
    post(root);
    answer.push_back(ans1);
    answer.push_back(ans2);

    return answer;
}