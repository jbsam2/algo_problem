#include <bits/stdc++.h>

using namespace std;

int solution(vector<vector<int>> board)
{
    int answer=0,oldanswer;
    int size=board.size(),i,j,k,l,m;
    int diri[5][3]={{1,1,1},{1,2,2},{1,2,2},{1,1,1},{1,1,1}};
    int dirj[5][3]={{0,1,2},{0,0,-1},{0,0,1},{0,-1,-2},{-1,0,1}};
    do 
    {
        oldanswer=answer;
        for(i=0;i<size-1;i++) 
        {
            for(j=0;j<size;j++) 
            {
                if(board[i][j]) 
                {
                    for(k=0;k<5;k++) 
                    {
                        for(l=0;l<3;l++)
                            if((j+dirj[k][l]<0)||(j+dirj[k][l]>=size)||(i+diri[k][l]>=size)||(board[i][j]!=board[i+diri[k][l]][j+dirj[k][l]])) 
                            	break;
                        if(l==3) 
                        {
                            for(l=0;l<3;l++) 
                            {                      
                                for(m=i+diri[k][l]-1;m>=0;m--) 
                                	if(board[m][j+dirj[k][l]]) 
                                		break;
                                if(m>=0&&board[m][j+dirj[k][l]]!=board[i][j]) 
                                	break;
                            }
                            if(l==3)
                            {
                                answer++;
                                board[i][j]=0;
                                for(l=0;l<3;l++) 
                                	board[i+diri[k][l]][j+dirj[k][l]]=0;
                            }
                            break;
                        }
                    }
                }
            }
        }
    }while(answer!=oldanswer);
    return answer;
}