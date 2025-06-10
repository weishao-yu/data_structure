while True:
    try:
        n = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))

        mapping = {num: i for i, num in enumerate(A)}

        pre = n + 1
        ans = True
        inc = False

        for num in B:
            idx = mapping[num]
            if inc and idx < pre:
                ans = False
                break
            if idx > pre:
                inc = True
            pre = idx

        print("Success" if ans else "Fail")

    except EOFError:
        break
