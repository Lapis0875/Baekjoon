try:
    while line := input():
        print(sum(map(int, line.split(' '))))
except EOFError:
    pass
