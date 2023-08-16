from sys import stdin
from typing import Final

A, B, C = map(int, stdin.readline().split(" "))
D: Final[int] = int(stdin.readline())

ONE_DAY: Final[int] = 86400
ONE_HOUR: Final[int] = 3600
ONE_MINUTE: Final[int] = 60

# day: int = D // ONE_DAY           # 하루가 넘어간 것은 날짜 고려를 하지 않으므로 버린다.
D %= ONE_DAY
hour: int = D // ONE_HOUR
D %= ONE_HOUR
minute: int = D // ONE_MINUTE
D %= ONE_MINUTE                     # remaning seconds

# print(f"DEBUG: hour={hour}, min={minute}, seconds={D}")

upper: int = 0
C += D
if C >= 60:
    C -= 60
    upper = 1

B += minute + upper
upper = 0
if B >= 60:
    B -= 60
    upper = 1

A += hour + upper
if A >= 24:
    A -= 24

print(A, B, C)