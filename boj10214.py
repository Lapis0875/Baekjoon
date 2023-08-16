from sys import stdin
from typing import Final
T: Final[int] = int(stdin.readline())

for _ in range(T):
    yonsei: int = 0
    korea: int = 0
    for _ in range(9):
        y, k = map(int, stdin.readline().split())
        yonsei += y
        korea += k
    if korea > yonsei:
        print("Korea")
    elif yonsei > korea:
        print("Yonsei")
    else:
        print("Draw")