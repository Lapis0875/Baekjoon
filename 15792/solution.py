from decimal import Decimal, setcontext, Context
setcontext(Context(prec=2000))
a, b = map(int, input().split(' '))
print(f'{Decimal(a)/Decimal(b)}'[:2000])