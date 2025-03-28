T = int(input())

for _ in range(T):
    N = int(input())
    if N == 0:
        print(0)
        continue
    if N == 1:
        print(1)
        continue
    result = []
    for n in range(9, 1, -1):
        while N % n == 0:
            result.append(n)
            N //= n
    if N == 1:
        result.reverse()
        print("".join(map(str, result)))
    else:
        print(-1)

# continue 無視同層級接下來的操作，直接跳到下一個迴圈