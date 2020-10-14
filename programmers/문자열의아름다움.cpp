#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll solution(string s) {
    if (s.size() == 1) return 0;
    ll ans = 0, count = 1;
    for (int i = s.size()-1; i >= 1; --i) {
        ans += (i*count);
        ++count;
    }
    vector<vector<int>> idx(26);
    for (int i = 0; i < s.size(); ++i) {
        idx[s[i] - 'a'].push_back(i);
    }

    for (int i = 0; i < 26; ++i) {
        if (idx[i].size() < 2) continue;
        vector<int> series(idx[i].size() + 1);
        int prev = idx[i][0];
        int count = 1;
        for (int j = 1; j < idx[i].size(); ++j) {
            int &curr = idx[i][j];
            if ((curr - prev) == 1) {
                ++count;
            }
            else {
                ++series[count];
                count = 1;
            }
            prev = curr;
        }
        ++series[count];

        for (int j = 1; j < idx[i].size(); ++j) {
            int count = 0;
            for (int k = j; k < series.size(); ++k) {
                count += series[k]*(k-j+1);
            }
            if (count == 0) continue;
            ans -= (ll)count*(count-1)/2;
        }
    }
    return max(ans, (ll)0);
}