while True:
    try:

        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break

        x = []
        for i in range(a, b+1):
            if (i**0.5).is_integer():
                x.append(i)
        print(len(x))
    except EOFError:
        break
