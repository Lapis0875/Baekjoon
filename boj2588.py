# boj 2588 "곱셈" (Bronze III)
from sys import stdin

N = int(stdin.readline())
M = int(stdin.readline())

A = M // 100
M %= 100

B = M // 10
M %= 10

print(P := N * M)
print(Q := N * B)
print(R := N * A)
print(P + Q * 10 + R * 100)
