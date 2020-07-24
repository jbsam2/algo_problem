#include <bits/stdc++.h>

using namespace std;

bitset<200009> bs[2];

int get(int n)
{
  int i=0, c;

  bs[n].reset();
  for (; (c=getchar()) != '\n'; i++)
    if (c == 'M') bs[n][i] = 1;

  return i;
}

void run()
{
  int ans=0, l = get(0);

  l = get(1) - l + 1;
  while (l--) {
    if (!(bs[0] & bs[1]).any()) ans++;
    bs[1] >>= 1;
  }
  printf("%d\n", ans);
}

int main()
{
  int t;
  scanf("%d\n", &t);
  while (t--) run();
}


#include <cstdio>
#include <string.h>
using namespace std;

char member[200001];
char fen[200001];
long membit[64][3127];
long fenbit[3127];

int main() {
  int tc;
  scanf("%d", &tc);
  while(tc-- > 0){
    memset(membit, 0, sizeof(membit));
    memset(fenbit, 0, sizeof(fenbit));
    scanf("%s", member);
    scanf("%s", fen);

    // Member
    int mIdx=0;
    while(member[mIdx] != '\0'){
      if(member[mIdx] == 'M'){
        // shift member bit (1~63)
        for(int shift=0; shift<64; shift++){
          membit[shift][(shift+mIdx)/64] |= 1l << (63-((shift+mIdx)&63));
        }
      }
      mIdx++;
    }
    // Fen
    int fIdx=0;
    while(fen[fIdx] != '\0'){
      if(fen[fIdx] == 'M'){
        fenbit[fIdx/64] |= 1l << (63-(fIdx&63));
      }
      fIdx++;
    }

    // bit matching between member with fen
    int hugCnt = 0;
    for(int i=0; i<fIdx-mIdx+1; i++){
      bool hug = true;
      int sh = (i & 63);
      for(int j=0; j<((mIdx+63)/64)+1; j++){
        if((membit[sh][j] & fenbit[i/64 + j]) != 0){
          hug = false;
          break;
        }
      }
      if(hug)
        hugCnt++;
    }
    printf("%d\n", hugCnt);
  }
  return 0;
}