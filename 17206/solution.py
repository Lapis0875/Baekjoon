T: int = int(input())
numbers = map(int, input().split(' '))
for N in numbers:
    print(
        sum(range(1, int(N / 3) + 1)) * 3
        + sum(range(1, int(N / 7) + 1)) * 7
        - sum(range(1, int(N / 21) + 1)) * 21
    )