numbers = []
for _ in range(10):
    numbers.append(int(input()))

print(len(set(map(lambda n: n % 42, numbers))))
