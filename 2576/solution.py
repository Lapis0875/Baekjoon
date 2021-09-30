number_count: int = int(input())
numbers: tuple[int] = tuple(map(int, input().split(' ')))
match_count: int = int(input())
matches = map(int, input().split(' '))

for result in map(
        lambda m: any(map(
            lambda n: n == m,
            numbers
        )),
        matches
):
    print(result.__int__())
