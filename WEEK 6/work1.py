def f(a, b):
    num = 0
    i = 1
    while i * i <= b:
        if i * i >= a:
            num += 1
        i += 1
    return num

while True:
    try:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        print(f(a, b))
    except EOFError:
        break
