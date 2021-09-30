count: int = int(input())
for _ in range(count):
    case = input()
    answer_streak: int = 0
    score: int = 0
    for char in case:
        if char == 'O':
            answer_streak += 1
            score += answer_streak
        else:
            answer_streak = 0
    print(score)
