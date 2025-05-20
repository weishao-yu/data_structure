while True:
    try:
        a, b = map(int, input().split())
        count = 0
        original_a = a
        original_b = b

        if a > b:
            a, b = b, a

        for i in range(a, b+1):
            n = i
            cycle = 1

            while n != 1:
                if n % 2 == 0:
                    n //= 2
                else:
                    n = 3 * n + 1
                cycle += 1

            count = max(count, cycle)

        print(f"{original_a} {original_b} {count}")
    except EOFError:
        break
