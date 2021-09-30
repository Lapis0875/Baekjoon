from string import ascii_lowercase
text = input()
print(' '.join(map(lambda c: str(text.index(c)) if c in text else '-1', ascii_lowercase)))