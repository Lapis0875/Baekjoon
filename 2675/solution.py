def repeat_string(R: int, S: str) -> str:
    result: str = ''
    for char in S:
        result += char * R
    return result


cases: int = int(input())

for _ in range(cases):
    R, S = input().split(' ')
    print(repeat_string(int(R), S))
