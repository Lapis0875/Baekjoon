from sys import stdin
from typing import Callable, Final

def DFS(n: int) -> None:
    """트리를 깊이 우선 탐색(DFS)로 순회하며, 제거할 노드와 그 자식 노드들을 모두 트리에서 제거한다.
    DFS를 쓰는 이유 : 탐색을 시작하는 노드의 자식노드부터 우선 탐색하기 때문에, 자식 노드를 제거하려는 문제의 의도와 걸맞다.

    Args:
        n (int): 제거할 노드의 번호.
    """
    Tree[n] = ERASED        # 현재 노드를 제거한다.
    # print(f">>> DFS({n})\n    {Tree}\n")
    
    for i in range(N):          # 트리 전체를 순회하며
        if Tree[i] != ERASED and n == Tree[i]:    # 만약 순회중인 노드가 제거된 노드를 부모로 할 때
            # print(f"    -> {n}번 노드의 자식 노드인 {i}번째 노드를 제거한다.")
            DFS(i)          # DFS로 해당 노드도 제거한다.

# 상수 정의
input: Final[Callable[[int], str]] = stdin.readline              # 느린 내장함수 input 대신, sys 모듈의 stdin.readline을 input 대용으로 사용한다.
ERASED: Final[int] = -2

N: Final[int] = int(input())
Tree: Final[list[int]] = [ int(v) for v in input().split() ]
erase: Final[int] = int(input())

DFS(erase)

# print(Tree)
cnt: int = 0
for i in range(N):
    if Tree[i] != ERASED and i not in Tree:       # i번째 노드가 지워지지 않았고, 자신을 부모로 하는 노드가 트리 안에 없으면
        cnt += 1                            # 말단 노드이다!

print(cnt)