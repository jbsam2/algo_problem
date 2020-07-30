#include <bits/stdc++.h> 
using namespace std;
 
int check(int n)
{ if(1 <= n && n <= 12) return true; else return false;}
 
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);
     
    int t;
    cin >> t;
    
    for(int tc=1;tc<=t;tc++)
    {
        int date;
        cin >> date;
        int tmp1 = date/100;
        int tmp2 = date%100;
        bool chk1 = check(tmp1);
        bool chk2 = check(tmp2);
        cout<<"#"<<tc<<" ";
        if(chk1&&chk2) cout<<"AMBIGUOUS";
        else if(chk1&&!chk2) cout<<"MMYY";
        else if(!chk1&&chk2) cout<<"YYMM";
        else if(!chk1&&!chk2) cout<<"NA";
        cout << "\n";
    } 
    return 0;
}