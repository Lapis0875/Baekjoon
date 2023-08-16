from math import sqrt
from sys import stdin
from typing import Final

M: Final[int] = 10_000_000
sqrtM = int(sqrt(M))

primes = [False, False]
primes.extend(True for _ in range(sqrtM))
for i in range(2, sqrtM):
    if primes[i]:
        j: int = 2
        while (x := i * j) <= sqrtM:
            primes[x] = False
            j += 1

primes = [i for i in range(sqrtM + 1) if primes[i]]
primeCnt = len(primes)
div: int = 0
N = int(stdin.readline())
while N > 1:
    if div == primeCnt:
        print(N)
        break
    divisor = primes[div]
    if N % divisor == 0:
        print(divisor)
        N //= divisor
    else:
        div += 1