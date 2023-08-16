from sys import stdin
from typing import Final

S: Final[int] = int(stdin.readline())

# 이분탐색
left: int = 1
right: int = S
answer: int = -1
while (left <= right):
    mid: int = (left + right) // 2
    if mid * (mid + 1) // 2 > S:        # 1부터 mid까지의 자연수 합 공식. N의 최대값이 필요하므로, 1부터의 합을 계산하는 방식을 택했다.
        right = mid - 1
    else:
        answer = mid
        left = mid + 1

print(answer)
