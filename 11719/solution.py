# with open(0, 'w+', encoding='utf-8') as f:    # open stdin
#     for line in f:
#         print(line[:100])
try:
    for _ in range(100):
        line = input()
        print(line)
except EOFError:
    pass