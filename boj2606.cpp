#include <iostream>
#include <vector>

using namespace std;

vector<int>* graph;
bool* visited;

int dfs(int idx)
{
    visited[idx] = true;
    int u, cnt = 1;
    for (int i = 0; i < graph[idx].size(); i++)
    {
        u = graph[idx][i];
        if (!visited[u])
            cnt += dfs(u);
    }
    return cnt;
}

int main()
{
    int N, M, u, v;
    scanf("%d\n", &N);
    graph = new vector<int>[N+1];
    visited = new bool[N+1];

    scanf("%d\n", &M);
    for (int i = 0; i < M; i++)
    {
        scanf("%d %d", &u, &v);
        graph[u].push_back(v);
        graph[v].push_back(u);    
    }
    printf("%d\n", dfs(1) - 1);     // 1번 컴퓨터만 개수에서 제외.

    return 0;
}
