N: int = int(input())
if N % 2 == 0:
    print('I LOVE CBNU')
else:
    print('*'*N)
    M = (N + 1) // 2
    for i in range(M):
        if i == 0:
            print(' ' * (M-i-1) + '*')
        else:
            print(' ' * (M-i-1) + '*' + ' ' * (2*i-1) + '*')
