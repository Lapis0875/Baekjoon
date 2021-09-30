"""
백준 2576번 문제
Bronze III

Question :
7개의 자연수가 주어질 때, 이들 중 홀수인 자연수들을 모두 골라 그 합을 구하고, 고른 홀수들 중 최솟값을 찾는 프로그램을 작성하시오.
예를 들어, 7개의 자연수 12, 77, 38, 41, 53, 92, 85가 주어지면 이들 중 홀수는 77, 41, 53, 85이므로 그 합은
77 + 41 + 53 + 85 = 256
이 되고,
41 < 53 < 77 < 85
이므로 홀수들 중 최솟값은 41이 된다.

Input :
입력의 첫째 줄부터 일곱 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100보다 작다.

Output :
홀수가 존재하지 않는 경우에는 첫째 줄에 -1을 출력한다. 홀수가 존재하는 경우 첫째 줄에 홀수들의 합을 출력하고, 둘째 줄에 홀수들 중 최솟값을 출력한다.

Condition :
- 시간제한 1초
- 메모리 제한 128 MB

Test Cases:
  Case 1:
    Input:
      12
      77
      38
      41
      53
      92
      85
    Output:
      256
      41
  Case 2:
    Input:
      2
      4
      20
      32
      6
      10
      8
    Output:
      -1
"""

from timeit import timeit
from functools import partial

numbers = []
for _ in range(7):
    numbers.append(int(input()))


def solution():
    odds = tuple(filter(lambda n: n % 2 == 1, numbers))
    res = sum(odds, 0)
    if res == 0:
        print(-1)
        return
    print(res)
    print(min(odds))


duration = timeit(solution, number=1)
print(f'sol1 : {duration:.12f} seconds elapsed/')
