from collections import Counter


def solution(text: str):
    cnt = Counter(text.upper())
    counted = cnt.most_common()
    if len(counted) == 1 or counted[0][1] != counted[1][1]:
        answer = counted[0][0]
    else:
        answer = '?'
    print(answer)
    return answer


test_cases = (
    ('Mississipi', '?'),
    ('zZa', 'Z'),
    ('z', 'Z'),
    ('baaa', 'A'),
)
for text, answer in test_cases:
    result = solution(text)
    print(result == answer)
