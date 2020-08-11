#include <iostream>
using namespace std;
int m[128];

void decoder(char* encode,char* decode)
{
    int bit,pos=0,pos2=0;
    while(encode[pos])
    {
        bit = m[encode[pos++]]<<18;
        bit += m[encode[pos++]]<<12;
        bit += m[encode[pos++]]<<6;
        bit += m[encode[pos++]];
        decode[pos2++]=bit>>16&0xFF;
        decode[pos2++]=bit>>8&0xFF;
        decode[pos2++]=bit&0xFF;
    }
    decode[pos2]=0;
}

int main()
{
    for(int i=0;i<26;i++)m['A'+i]=i;
    for(int i=0;i<26;i++)m['a'+i]=26+i;
    for(int i=0;i<11;i++)m['0'+i]=52+i;
    m['+']=62,m['/']=63;
    int tc;
    cin>>tc;
    char encoded[100000],decoded[100000];
    for(int t=1;t<=tc;t++)
    {
        cin>>encoded;
        decoder(encoded, decoded);
        printf("#%d %s\n",t,decoded);
    }
}
