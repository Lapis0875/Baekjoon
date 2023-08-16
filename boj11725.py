from collections import deque
from sys import stdin
from typing import Final

DEFAULT: Final[int] = 0
N: Final[int] = int(stdin.readline())
Tree: Final[list[list[int]]] = [ [] for _ in range(N + 1) ]
Parent: Final[list[int]] = [ DEFAULT for _ in range(N + 1) ]

for _ in range(N - 1):
    u, v = map(int, stdin.readline().split())
    Tree[u].append(v)
    Tree[v].append(u)

def DFS(node: int):
    for n in Tree[node]:
        if Parent[n] == DEFAULT:
            Parent[n] = node
        DFS(node)

def BFS():
    queue: deque[int] = deque([1])  # 루트 노드인 1을 미리 큐에 넣어둔다.
    while queue:        # 큐가 비어있지 않을 때 계속 반복하며,
        node = queue.popleft()
        for n in Tree[node]:
            if Parent[n] == DEFAULT:
                Parent[n] = node
                queue.append(n)

BFS()

for n in Parent[2:]:
    print(n)