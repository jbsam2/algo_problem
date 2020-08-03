#include <iostream>
using namespace std;
int m[128];

void decode(char* encode, char* decode)
{
    int bits, pos=0, pos2=0;
    while(encode[pos])
    {
        bits = m[encode[pos++]] << 18;
        bits += m[encode[pos++]] << 12;
        bits += m[encode[pos++]] << 6;
        bits += m[encode[pos++]];
        decode[pos2++] = bits>>16 & 0xFF;
        decode[pos2++] = bits>>8 & 0xFF;
        decode[pos2++] = bits & 0xFF;
    }
    decode[pos2] = 0;
}

int main()
{
    for(int i=0; i<26; i++) m['A'+i]=i;
    for(int i=0; i<26; i++) m['a'+i]=26+i;
    for(int i=0; i<11; i++) m['0'+i]=52+i;
    m['+'] = 62;
    m['/'] = 63;
    int T;
    scanf("%d", &T);
    char encoded[100000];
    char decoded[100000];
    for(int tc=1; tc<=T; tc++)
    {
        scanf("%s", encoded);
        decode(encoded, decoded);
        printf("#%d %s\n", tc, decoded);
    }
}
