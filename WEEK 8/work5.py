K = int(input())
for _ in range(K):
    n = int(input())
    original = [input().strip() for _ in range(n)]
    target = [input().strip() for _ in range(n)]

    result = []
    idx = n - 1  # 從原始的最後開始往前比

    for i in range(n - 1, -1, -1):
        while idx >= 0 and original[idx] != target[i]:
            result.append(original[idx])
            idx -= 1
        if idx >= 0:
            idx -= 1

    for name in (result):
        print(name)
    print()
