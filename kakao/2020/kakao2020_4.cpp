#include <bits/stdc++.h>
using namespace std;

int tonum(char ch){return (ch=='?')?26:(ch-'a');}

struct Trie
{
    int count;
    Trie* child[27];
    bool end;
    Trie():end(false),count(0)
    {memset(child,0,sizeof(child));}
    ~Trie()
    {for(int i=0;i<27;i++)if(child[i])delete child[i];}
    void insert(const char *key)
    {
        if(*key==0) end=true;
        else
        {
            int next=tonum(*key);
            if(child[next]==NULL)child[next]=new Trie();
            child[next]->insert(key+1);
        }
    }
    void find(const char *key)
    {
        if(*key==0){count++;return;}
        int next=tonum(*key);
        if(child[26]!=NULL)child[26]->find(key+1);
        if(child[next]!=NULL)child[next]->find(key+1);
    }
    int get_count(const char *key)
    {
        if(*key==0)return count;
        int next=tonum(*key);
        if(child[next]==NULL)return 0;
        return child[next]->get_count(key+1);
    }
};

vector<int> solution(vector<string> words, vector<string> queries)
{
    vector<int> answer;
    Trie sol;
    for(auto querie:queries)sol.insert(querie.c_str());
    for(auto word:words)sol.find(word.c_str());
    for(auto querie:queries)answer.push_back(sol.get_count(querie.c_str()));
    return answer;
}



#include <bits/stdc++.h>
using namespace std;

bool match(string &query,string &word)
{
    if(query.length()!=word.length())return 0;
    for(int i=0;i<query.length();i++)if(query[i]!='?'&&query[i]!=word[i])return 0;
    return 1;
}

void create_map(vector<string> &words,unordered_map<string,int> &map)
{
    for(string &word:words)
    {
        for(int i=0;i<word.length();++i)
        {
            map[word.substr(0,i)+string(word.length()-i,'?')]++;
            map[string(i,'?')+word.substr(i)]++;
        }
    }
}

vector<int> solution(vector<string> words,vector<string> queries)
{
    unsigned long max_length=0;
    for(string &word:words)max_length=max(max_length,word.length());
    vector<int> answer;
    if(max_length>1000)
    {
        for(string &query:queries)
        {
            int num_matched=0;
            for(string &word:words)if(match(query,word))num_matched++;
            answer.push_back(num_matched);
        }
    }
    else
    {
        unordered_map<string,int> map;
        create_map(words,map);
        for(string &query:queries)answer.push_back(map[query]);
    }
    return answer;
}