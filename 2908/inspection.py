from timeit import timeit

numbers: list[str] = input().split(' ')


def reversed_str_sol():
    a, b = map(lambda v: int(''.join(list(reversed(v)))), numbers)
    print(a if a >= b else b)


def reverse_int(v: str) -> int:
    v = int(v)
    hundred = v // 100
    ten = (v % 100) // 10
    one = v % 10
    new = one * 100 + ten * 10 + hundred
    return new


def int_reverse_sol():
    a, b = map(reverse_int, numbers)
    print(a if a >= b else b)


print(f'string reverse sol took {timeit(reversed_str_sol, number=1):.12f} seconds')
print(f'int reverse sol took {timeit(int_reverse_sol, number=1):.12f} seconds')
