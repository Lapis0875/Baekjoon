from collections import Counter
from sys import stdin

c: Counter[int] = Counter(map(int, stdin.readline().split()))
cnt: list[tuple[int, int]] = c.most_common()

if cnt[0][1] == 3:      # 세 수가 모두 같다.
    print(10000 + cnt[0][0] * 1000)
elif cnt[0][1] == 2:    # 같은 눈이 2개.
    print(1000 + cnt[0][0] * 100)
else:
    print(sorted(c.elements(), reverse=True)[0] * 100)