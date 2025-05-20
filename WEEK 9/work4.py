while True:
    try:
        n = int(input())
        before = list(map(int, input().split()))
        after = list(map(int, input().split()))
        l, r = 0, n - 1
        possible = True
        for x in after:
            if l <= r and x == before[l]:
                l += 1
            elif l <= r and x == before[r]:
                r -= 1
            else:
                possible = False
                break
        print("Success" if possible else "Fail")
    except EOFError:
        break
