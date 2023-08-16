# boj 2914 "저작권" (Bronze III)
"""
Solution)
894의 멜로디, 38개 곡 -> 23.53, 올림해서 24

예제 1의 두 수는 38과 24.
저작권이 있는 멜로디의 평균값을 X라 하면, 이 예제에서 X는 23 < X <= 24 의 조건을 만족한다.
이때, 저작권이 있는 멜로디의 최소 개수를 Y라 하면
23 * 38 < Y = 38 * X < 24 * 38
따라서, 정수 Y의 최솟값은 23 * 38 + 1이다.
"""
from sys import stdin
A, I = map(int, stdin.readline().split())
print(A * (I - 1) + 1)