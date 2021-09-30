max_value: int = 0
index: int = 0
for i in range(9):
    num = int(input())
    if num > max_value:
        max_value = num
        index = i + 1
print(max_value, index, sep='\n')