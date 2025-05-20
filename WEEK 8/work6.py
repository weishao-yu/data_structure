def func(n):
    if n == 1:
        return 1
    else:
        return n * func(n - 1)

def calt(n):
    return func (2 * n) // (func(n) * func(n + 1))


while True:
    try:
        n = int(input())
        if n == 0:
            break
        print(calt(n))
    except EOFError:
        break