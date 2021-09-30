def GCD(a: int, b: int):
    r = a % b
    if r == 0:
        return b
    return GCD(b, r)


case_count: int = int(input())
for _ in range(case_count):
    a, b = map(int, input().split(' '))
    gcd = GCD(a, b) if a >= b else GCD(b, a)
    print(int(a * b / gcd))
