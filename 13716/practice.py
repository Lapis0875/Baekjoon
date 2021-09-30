# const
from typing import Final
from sys import getsizeof
from timeit import timeit
from functools import partial, lru_cache
D: Final[int] = 10**9 + 7


def old_solution(n: int, k: int):
    print('n =', n, 'k =', k)
    cache: list[int] = [1, 1, 2]
    print('size of initial cache :', getsizeof(cache))

    def F(i: int) -> int:
        try:
            return cache[i]
        except IndexError:
            v = F(i-1) + F(i-2)
            cache.append(v)
            return v

    def A(i: int) -> int:
        return F(i) * (i ** k)

    # print('Manual for-loop result :')
    # sum_v: int = 0
    # for i in range(1, n+1):
    #     v_i = A(i)
    #     print(f'F(i={i}) = {F(i)}')
    #     print(f'A(i={i}, k={k}) = {v_i}')
    #     sum_v += v_i
    # print('total sum :', sum_v)
    # print('remain :', sum_v % D)

    print('Short sum(map) result :')
    print(int(sum(map(A, range(1, n+1))) % D))
    print('size of current cache :', getsizeof(cache) / 1024, 'mb')
    from pprint import pprint
    # pprint(cache)


def solution(n: int, k: int):
    @lru_cache(maxsize=n)
    def F(i: int) -> int:
        if i < 2:
            return 1
        elif i == 2:
            return 2
        return F(i-1) + F(i-2)

    def A(i: int) -> int:
        return F(i) * i ** k

    print(sum(map(A, range(1, n+1))))

# while (input_str := input()) != 'quit':
#     try:
#         n, k = map(int, input_str.split(' '))
#         solution(n, k)
#     except Exception:
#         continue


# n, k = map(int, input().split(' '))
n = 10**9
k = 20
time = timeit(stmt=partial(solution, n=n, k=k), number=1)
print(f'`{time}` seconds elapsed.')
# solution(n, k)
