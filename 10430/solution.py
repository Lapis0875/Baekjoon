a, b, c = map(int, input().split(' '))
ac = a % c
bc = b % c
print((a + b) % c)
print((ac + bc) % c)
print((a * b) % c)
print((ac * bc) % c)
