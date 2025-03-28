while True:
    try:
        a, b = map(int, input().split())
        result = a * b * 2
        print(result)
    except EOFError:
        break