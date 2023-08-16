from sys import stdin
from typing import Final

T: Final[int] = int(stdin.readline())
A: Final[int] = 300
B: Final[int] = 60
C: Final[int] = 10

a: int = 0
b: int = 0
c: int = 0

while T >= C:
    if T >= A:
        T -= A
        a += 1
    elif T >= B:
        T -= B
        b += 1
    elif T >= C:
        T -= C
        c += 1
        
if T == 0:
    print(a, b, c)
else:
    print(-1)