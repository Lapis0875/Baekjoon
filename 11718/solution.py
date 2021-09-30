try:
    while line := input():
        print(line)
except EOFError:
    pass