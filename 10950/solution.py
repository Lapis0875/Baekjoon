case_count: int = int(input())
cases: list[tuple[int, int]] = []

for _ in range(case_count):
    cases.append(tuple(map(int, input().split(' '))))

for a, b in cases:
    print(a + b)
