#include <bits/stdc++.h>
using namespace std;

int solution(vector<vector<int>> board, vector<int> moves)
{
    int answer=0;
    stack<int> basket;

    for(int i=0;i<moves.size();i++)
    {
        int check=moves[i]-1;
        for(int j=0;j<board.size();j++)
        {
            if(board[j][check])
            {
                if(!basket.empty()&&basket.top()==board[j][check])
                {
                    basket.pop();
                    answer+=2;
                }
                else
                    basket.push(board[j][check]);
                board[j][check]=0;
                break;
            }
        }
    }
    return answer;
}