#include <iostream>
#include <vector>
#include <queue>
#define MAX_POS 200000
using namespace std;

int dist[MAX_POS + 1];

int bfs(int N, int K)
{
    queue<int> q;
    dist[N] = 0;
    q.push(N);

    while(!q.empty() && dist[K] != 0)
    {
        if (N + 1 < MAX_POS)
            q.push(N - 1);
        if (N < MAX_POS)
            q.push(N + 1);
        if 
    }
}

int main(void)
{
    int N, K;
    scanf("%d %d", &N, &K);
    return 0;
}
