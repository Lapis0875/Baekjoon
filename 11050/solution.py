from math import factorial


def C(n: int, k: int) -> float:
    return factorial(n) / (factorial(k) * factorial(n-k))


N, K = map(int, input().split(' '))
print(int(C(N, K)))
