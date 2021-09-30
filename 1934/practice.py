"""
백준 1934번 문제
Silver V

Question :
두 자연수 A와 B에 대해서, A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수라고 한다.
이런 공배수 중에서 가장 작은 수를 최소공배수라고 한다. 예를 들어, 6과 15의 공배수는 30, 60, 90등이 있으며, 최소 공배수는 30이다.
두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.

Input :
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다.
둘째 줄부터 T개의 줄에 걸쳐서 A와 B가 주어진다. (1 ≤ A, B ≤ 45,000)

Output :
첫째 줄부터 T개의 줄에 A와 B의 최소공배수를 입력받은 순서대로 한 줄에 하나씩 출력한다.

Condition :
- 시간제한 1초
- 메모리 제한 128 MB

Test Cases:
  Case 1:
    Input:
      3
      1 45000
      6 10
      13 17
    Output:
      45000
      30
      221
"""

from timeit import timeit
from functools import partial


def solution(a: int, b: int):
    """
    :input: 10,000이하의 두 개의 자연수.
    :output: 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력힘.
    """
    def GCD(a: int, b: int):
        """
        최대공약수를 계산합니다.
        a >= b
        """
        r = a % b
        if r == 0:
            return b
        return GCD(b, r)

    def LCM(a: int, b: int, gcd: int) -> int:
        """
        최소공배수를 계한합니다.
        a >= b
        """
        return int((a * b) / gcd)

    gcd = GCD(a, b) if a >= b else GCD(b, a)
    print(LCM(a, b, gcd))


def test_case():
    test_cases = (
        (1, 45000),
        (6, 10),
        (13, 17),
    )
    for a, b in test_cases:
        print(f'A={a}, B={b}')
        duration = timeit(partial(solution, a=a, b=b), number=1)
        print(f'{format(duration, ".8f")} seconds elapsed/')


def manual_run():
    case_count: int = int(input())
    for _ in range(case_count):
        a, b = map(int, input().split(' '))
        print(f'Case = ({a}, {b})')
        duration = timeit(partial(solution, a=a, b=b), number=1)
        print(f'{duration:.4f} seconds elapsed/')


manual_run()
