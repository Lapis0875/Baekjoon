"""
백준 2609번 문제
Silver V

Question :
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

Input :
첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

Output :
첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

Condition :
- 시간제한 1초
- 메모리 제한 128 MB

Test Cases:
  Case 1:
    Input:
      24 18
    Output:
      6
      72
"""

from timeit import timeit
from functools import partial


def raw_thought(a: int, b: int):
    """
    어떤 알고리즘을 써야하는지 모르는 상황에서, 직접 생각해 부딪혀본 방법입니다. 정말 단순하게 반복문을 이용합니다.
    시간초과가 발생하는 방식입니다.
    :input: 10,000이하의 두 개의 자연수.
    :output: 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력힘.
    """
    if a == b:
        # speed-up for special cases.
        print(a)
        print(a)
        return
    if a >= b:
        bigger_one = a
        small_one = b
    else:
        bigger_one = b
        small_one = a

    # 최대공약수 구하기
    for i in filter(lambda i: small_one % i == 0, range(small_one, 1, -1)):
        # i는 a의 약수
        if bigger_one % i == 0:
            # i는 b의 약수이기도 하다!
            # => 최소공약수
            print(i)
            break
    else:
        print(1)

    # 최소공배수 구하기
    for i in filter(lambda i: i % bigger_one == 0, range(bigger_one, a*b+1)):
        # i는 a의 배수
        if i % small_one == 0:
            # i는 b의 배수이기도 하다!
            # => 최소공배수
            print(i)
            break


def euclidean_algorithm(a: int, b: int):
    def GCD(a: int, b: int):
        """
        최대공약수를 계산합니다.
        a >= b
        """
        r = a % b
        if r == 0:
            return b
        return GCD(b, r)

    def LCM(a: int, b: int, gcd: int):
        """
        최소공배수를 계한합니다.
        a >= b
        """
        return (a * b) / gcd

    gcd = GCD(a, b) if a >= b else GCD(b, a)
    print(gcd)
    print(LCM(a, b, gcd))


def solution(a: int, b: int):
    """
    :input: 10,000이하의 두 개의 자연수.
    :output: 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력힘.
    """
    euclidean_algorithm(a, b)


def test_case():
    test_cases = (
        (24, 18),
        (6, 6),
        (12, 36),
        (50, 25),
        (11, 3),
    )
    for a, b in test_cases:
        print(f'A={a}, B={b}')
        duration = timeit(partial(solution, a=a, b=b), number=1)
        print(f'{format(duration, ".8f")} seconds elapsed')


def manual_run():
    while (input_str := input()) != 'quit':
        a, b = map(int, input_str.split(' '))
        print(f'A={a}, B={b}')
        duration = timeit(partial(solution, a=a, b=b), number=1)
        print(f'{duration:.4f} seconds elapsed/')


manual_run()
