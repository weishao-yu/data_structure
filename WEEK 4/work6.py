def calc(n):
    while n >= 10:
        sum_digits = 0
        while n > 0:
            sum_digits += n % 10
            n //= 10
        n = sum_digits
    return n

while True:
    try:
        line = input().strip()
        if line == "":
            break
        sum = 0
        n = int(line)
        if n == 0:
            break
        print(calc(n))
    except EOFError:
        break
