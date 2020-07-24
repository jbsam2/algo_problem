#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int cache[101][101];
string wildcard,filename;

int matchmemoized(int w,int f)
{
        int &result=cache[w][f];
        if(result!=-1)
                return result;
        if(w<wildcard.size()&&f<filename.size()&&(wildcard[w]=='?'||wildcard[w]==filename[f]))
                return result=matchmemoized(w+1,f+1);
        if(w==wildcard.size()&&f==filename.size())
                return result=1;
        if(wildcard[w]=='*')
        {
                if(matchmemoized(w+1,f)||(f<filename.size()&&matchmemoized(w,f+1)))
                        return result=1;
        }
        return result=0;
}
int main()
{
        int test;
        cin>>test;
        if(test<1||test>10)
                exit(-1);
        for(int j=0;j<test;j++)
        {
                vector<string> v;
                cin>>wildcard;
                int filenum;
                cin>>filenum;
                if(filenum<1||filenum>50)
                        exit(-1);
                for(int i=0;i<filenum;i++)
                {
                        memset(cache,-1,sizeof(cache));
                        cin>>filename;
                        if(matchmemoized(0,0)==1)
                                v.push_back(filename);
                }
                sort(v.begin(),v.end());
                for(int i=0;i<v.size();i++)
                        cout<<v[i]<<endl;
                cout<<endl;
        }
        return 0;
}

#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string pat, str;
int cache[100][101], lenPat, lenStr;

int solve(int i, int j) {
        if (i == lenPat)
                return j == lenStr;

        int &ret = cache[i][j];
        if (ret != -1) return ret;

        if (pat[i] == '*')
                return ret = solve(i + 1, j) || ((j < lenStr) && solve(i, j + 1));
        if (j < lenStr && (pat[i] == '?' || pat[i] == str[j]))
                return ret = solve(i + 1, j + 1);

        return ret = 0;
}

int main() {
        int nCase, n, res;
        vector<string> ans;

        cin >> nCase;
        for (int tc = 0; tc < nCase; ++tc) {
                ans.clear();

                cin >> pat >> n;
                lenPat = pat.size();
                for (int i = 0; i < n; ++i) {
                        memset(cache, 0xFF, sizeof(cache));

                        cin >> str;
                        lenStr = str.size();
                        res = solve(0, 0);
                        if (res)
                                ans.push_back(str);
                }

                sort(ans.begin(), ans.end());
                for (string s : ans)
                        cout << s << endl;
        }

        return 0;
}