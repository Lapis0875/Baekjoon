def reverse_int(v: str) -> int:
    v = int(v)
    hundred = v // 100
    ten = (v % 100) // 10
    one = v % 10
    new = one * 100 + ten * 10 + hundred
    return new


a, b = map(reverse_int, input().split(' '))
print(a if a >= b else b)