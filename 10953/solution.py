case_count: int = int(input())
for _ in range(case_count):
    a, b = map(int, input().split(','))
    print(a + b)
