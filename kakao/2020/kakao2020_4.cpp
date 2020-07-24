#include <string>
#include <vector>
#include <iostream>
#include <cstring>
using namespace std;

int toNum(char ch)
{
	if(ch=='?')return 26;
	return ch-'a';
}

struct Trie
{
	Trie* children[27];
	bool terminal;
	int cnt;
	Trie():terminal(false),cnt(0)
	{
		memset(children,0,sizeof(children));
	}
	~Trie()
	{
		for(int i=0;i<27;i++)
			if(children[i])
				delete children[i];
	}
	void insert(const char* key)
	{
		if(*key==0)
			terminal=true;
		else
		{
			int next=toNum(*key);
			if(children[next]==NULL)
				children[next]=new Trie();
			children[next]->insert(key+1);
		}
	}
	void find(const char* key)
	{
		if(*key==0)
		{
			cnt++;
			return;
		}
		int next=toNum(*key);
		if(children[26]!=NULL)
			children[26]->find(key+1);
		if(children[next]!=NULL)
			children[next]->find(key+1);
	}
	int get_cnt(const char* key)
	{
		if(*key==0)return cnt;
		int next=toNum(*key);
		if(children[next]==NULL)return 0;
		return children[next]->get_cnt(key+1);
	}
};

vector<int> solution(vector<string> words,vector<string> queries)
{
	vector<int> answer;
	Trie trie;
	for(int i=0;i<queries.size();i++)
		trie.insert(queries[i].c_str());
	for(int i=0;i<words.size();i++)
		trie.find(words[i].c_str());
	for(int i=0;i<queries.size();i++)
		answer.push_back(trie.get_cnt(queries[i].c_str()));
	return answer;
}

#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

bool match(string &query,string &word)
{
    if(query.length()!=word.length())
        return false;
    for(int i=0;i<query.length();++i)
        if(query[i]!='?'&&query[i]!=word[i])
            return false;
    return true;
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

    for(string &word:words)
        max_length=max(max_length,word.length());

    vector<int> answer;

    if(max_length>1000)
    {
        for(string &query:queries)
        {
            int num_matched=0;
            for(string &word:words)
                if(match(query,word))
                    num_matched++;
            answer.push_back(num_matched);
        }
    }
    else
    {
        unordered_map<string,int> map;
        create_map(words,map);
        for(string &query:queries)
            answer.push_back(map[query]);
    }
    return answer;
}