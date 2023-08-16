from sys import stdin
from typing import Final

A, B = map(int, stdin.readline().split(" "))
C: Final[int] = int(stdin.readline())

ONE_DAY: Final[int] = 1440
ONE_HOUR: Final[int] = 60

hour: int = (C % ONE_DAY) // ONE_HOUR
C %= ONE_HOUR                       # 남은 분 단위의 시간

# print(f"CEBUG: hour={hour}, min={minute}")

upper: int = 0
B += C
if B >= 60:
    B -= 60
    upper = 1

A += hour + upper
if A >= 24:
    A -= 24

print(A, B)