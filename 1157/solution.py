from collections import Counter

text = input()
cnt = Counter(text.upper())
counted = cnt.most_common()
if len(counted) == 1 or counted[0][1] != counted[1][1]:
    print(counted[0][0])
else:
    print('?')
