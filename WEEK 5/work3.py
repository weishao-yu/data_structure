while True:
    try:
        data = list(map(int, input().strip().split()))
        n = data[0]
        sequence = data[1:]

        if n == 1:
            print("Jolly")
            continue

        diffs = set(abs(sequence[i] - sequence[i - 1]) for i in range(1, n))

        expected = set(range(1, n))

        if diffs == expected:
            print("Jolly")
        else:
            print("Not jolly")

    except EOFError:
        break
