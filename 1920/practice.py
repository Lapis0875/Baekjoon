"""
백준 1920번 문제
Silver IV

Question :
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

Input :
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다.
다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다.
다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

Output :
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

Condition :
- 시간제한 2초
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

number_count: int = int(input())
numbers: tuple[int] = tuple(map(int, input().split(' ')))
match_count: int = int(input())
matches: tuple[int] = tuple(map(int, input().split(' ')))


def solution():
    for match in matches:
        print(1 if match in numbers else 0)


def solution2():
    for result in map(
        lambda m: any(map(
            lambda n: n == m,
            numbers
        )),
        matches
    ):
        print(result.__int__())


duration = timeit(solution, number=1)
print(f'sol1 : {duration:.12f} seconds elapsed/')
duration2 = timeit(solution2, number=1)
print(f'sol2 : {duration2:.12f} seconds elapsed/')
