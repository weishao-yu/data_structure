test_case = 0

while True:
    try:
        N = input().strip()
        if not N:
            continue
        N = int(N)

        sequence = list(map(int, input().strip().split()))

        test_case += 1
        is_b2_sequence = True

        for i in range(1, N):
            if sequence[i] <= sequence[i - 1]:
                is_b2_sequence = False
                break

        sum_set = set()
        if is_b2_sequence:
            for i in range(N):
                for j in range(i, N):
                    s = sequence[i] + sequence[j]
                    if s in sum_set:
                        is_b2_sequence = False
                        break
                    sum_set.add(s)
                if not is_b2_sequence:
                    break

        print(f"Case #{test_case}: ", end="")
        if is_b2_sequence:
            print("It is a B2-Sequence.")
        else:
            print("It is not a B2-Sequence.")
        print()

    except EOFError:
        break
