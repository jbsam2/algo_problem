class Solution {
  public int solution(int n, int s, int a, int b, int[][] fares) {
      int answer = Integer.MAX_VALUE;
      int[][] adj = new int[n+1][n+1];
      for(int i=0;i<n+1;i++)
      {
          for(int j=0;j<n+1;j++)
          {
              if(i==j)
                  adj[i][j] = 0;
              else
                  adj[i][j] = 1000000;
          }
      }
      for(int i=0;i<fares.length;i++)
      {
          int[] tmp = fares[i];
          adj[tmp[0]][tmp[1]] = tmp[2];
          adj[tmp[1]][tmp[0]] = tmp[2];
      }
      for(int k = 0;k<n+1;k++)
          for(int i=0;i<n+1;i++)
              for(int j=0;j<n+1;j++)
                  if(adj[i][j]>adj[i][k]+adj[k][j])
                      adj[i][j] = adj[i][k]+adj[k][j];
      for(int i=0;i<n+1;i++)
          answer = Math.min(answer,adj[s][i]+adj[i][a]+adj[i][b]);
      return answer;
  }
}