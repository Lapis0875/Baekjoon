from sys import stdin
from typing import Callable, Final
from collections import deque

# constants
input: Final[Callable[[int], str]] = stdin.readline

N, K = map(int, input().split())

def BFS(N: int, K: int) -> int:
    """BFS를 수행해, 수빈이가 좌표 N에서부터 동생의 좌표 K까지 탐색하는데 걸리는 시간을 계산한다.

    Args:
        N (int): _description_
        K (int): _description_

    Returns:
        int: _description_
    """
    time: int = 0
    
    if N == K:
        return time
    
    queue: deque[int] = deque([N])
    distance: list[int] = [-1] * 2 * N
    
    while queue:
        n: int = queue.popleft()
        
        if (n - 1) == K:
            
        
        queue.append(n + 1)
        queue.append(n - 1)
        queue.append(2 * n)
        time += 1

print(BFS(N, K))