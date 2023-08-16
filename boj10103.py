from sys import stdin
from typing import Final


C: int = 100                            # 창영
S: int = 100                            # 상덕
N: Final[int] = int(stdin.readline())   # 라운드 수
for _ in range(N):
    c, s = map(int, stdin.readline().split())
    if c > s:
        S -= c
    elif s > c:
        C -= s

print(C)
print(S)