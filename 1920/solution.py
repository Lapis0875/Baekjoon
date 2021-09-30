numbers = []
for _ in range(7):
    numbers.append(int(input()))
odds = tuple(filter(lambda n: n % 2 == 1, numbers))
res = sum(odds, 0)
if res == 0:
    print(-1)
else:
    print(res)
    print(min(odds))
