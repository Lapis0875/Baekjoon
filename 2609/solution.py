a, b = map(int, input().split(' '))


def GCD(a: int, b: int):
    """
    최대공약수를 계산합니다.
    a >= b
    """
    r = a % b
    if r == 0:
        return b
    return GCD(b, r)


def solution():
    """
    :input: 10,000이하의 두 개의 자연수.
    :output: 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력힘.
    """

    gcd = GCD(a, b) if a >= b else GCD(b, a)
    print(gcd)
    print(int(a * b / gcd))


solution()
