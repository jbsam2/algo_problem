#include <bits/stdc++.h>

using namespace std;

int cost[25][25][2];
int moveArr[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

struct node
{
    int y, x, dir;
};

bool operator>(node a, node b)
{
    return cost[a.y][a.x][a.dir] > cost[b.y][b.x][b.dir];
}

int solution(vector<vector<int>> board) {
    int answer = 0;
    int size = board.size();
    priority_queue < node, vector<node>, greater<node> > pq;

    for (int i = 0; i < 25; i++)
    {
        for (int j = 0; j < 25; j++)
        {
            cost[i][j][0] = 1<<29;
            cost[i][j][1] = 1<<29;
        }
    }

    if (board[0][1] == 0)
    {
        cost[0][1][1] = 100;
        pq.push({ 0, 1, 1 });
    }
    if (board[1][0] == 0)
    {
        cost[1][0][0] = 100;
        pq.push({ 1, 0, 0 });
    }

    while (!pq.empty())
    {
        node curr = pq.top();
        pq.pop();

        for (int i = 0; i < 4; i++)
        {
            int ny = curr.y + moveArr[i][0];
            int nx = curr.x + moveArr[i][1];
            int ndir = i / 2;
            if (ny < 0 || ny >= size || nx < 0 || nx >= size) continue;
            if (board[ny][nx] == 1) continue;
            int newCost = cost[curr.y][curr.x][curr.dir] + ((curr.dir == ndir) ? (100) : (600));
            if (cost[ny][nx][ndir] <= newCost) continue;
            cost[ny][nx][ndir] = newCost;
            pq.push({ny, nx, ndir});
        }
    }

    return min(cost[size - 1][size - 1][0], cost[size - 1][size - 1][1]);
}