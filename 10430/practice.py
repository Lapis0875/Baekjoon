from timeit import timeit
from functools import partial


def solution(a: int, b: int, c: int):
    ac = a % c
    bc = b % c
    print((a + b) % c)
    print((ac + bc) % c)
    print((a * b) % c)
    print((ac * bc) % c)


while (input_str := input()) != 'quit':
    a, b, c = map(int, input_str.split(' '))
    print(f'A={a}, B={b}, C={c}')
    duration = timeit(partial(solution, a=a, b=b, c=c), number=1)
    print(f'{duration} seconds elapsed/')
