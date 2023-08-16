#include <iostream>
#include <vector>
#include <queue>
#include <cstring>
#include <algorithm>

using namespace std;

vector<int>* graph;
bool* visited;

void dfs(int V)
{
    int u;
    visited[V] = true;
    printf("%d ", V);

    for (int i = 0; i < graph[V].size(); i++)
    {
        u = graph[V][i];
        if (!visited[u])
            dfs(u);
    }
}


void bfs(int V)
{
    queue<int> q;
    int v, u;
    q.push(V);

    while(!q.empty())
    {
        v = q.front();
        q.pop();
        
        if (!visited[v])
        {
            visited[v] = true;
            
            printf("%d ", v);

            for (int i = 0; i < graph[v].size(); i++)
            {
                u = graph[v][i];
                if (!visited[u])
                    q.push(u);
            }
        }
    }
}

int main(void)
{
    int N, M, V, u, v;
    scanf("%d %d %d\n", &N, &M, &V);

    graph = new vector<int>[N + 1];
    visited = new bool[N + 1];
    for (int i = 0; i < M; i++)
    {
        scanf("%d %d", &u, &v);
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    for (int i = 1; i <= N; i++)
    {
        sort(graph[i].begin(), graph[i].end());     // 인접리스트 오름차순 정렬.
    }

    dfs(V);
    putchar('\n');
    
    memset(visited, false, sizeof(bool) * (N + 1));
    bfs(V);
    putchar('\n');

    return 0;
}
