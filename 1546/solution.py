subject_count: int = int(input())
subjects: tuple[int] = tuple(map(int, input().split(' ')))
M = max(subjects)
new_scores: tuple[float] = tuple(map(lambda score: score / M * 100, subjects))
average: float = sum(new_scores) / subject_count
print(average)
