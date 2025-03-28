def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    f_prev2 = 0  # f(i-2)
    f_prev1 = 1  # f(i-1)
    for i in range(2, n + 1):
        f_current = f_prev1 + f_prev2  # f(i) = f(i-1) + f(i-2)
        f_prev2 = f_prev1  # 更新 f(i-2)
        f_prev1 = f_current  # 更新 f(i-1)
    return f_current


while True:
    try:
        n = int(input())
        print(fibonacci(n))
    except EOFError:
        break
