def f(long, i, j, key, n, m, data):
    while True:
        long += 2  # 擴展正方形邊長
        i -= 1
        j -= 1

        # 如果超出邊界，則返回最大可能的邊長
        if i < 0 or j < 0 or i + long > n or j + long > m:
            return long - 2

        # 檢查上方
        for a in range(long):
            if data[i + a][j] != key:
                return long - 2

        # 檢查右側
        for b in range(long):
            if data[i + long - 1][j + b] != key:
                return long - 2

        # 檢查下方
        for c in range(long):
            if data[i + long - 1 - c][j + long - 1] != key:
                return long - 2

        # 檢查左側
        for d in range(long):
            if data[i][j + long - 1 - d] != key:
                return long - 2


# 讀取測試案例數
t = int(input())

for _ in range(t):
    # 讀取矩陣大小 M, N 和查詢數量 Q
    n, m, q = map(int, input().split())
    print(n, m, q)

    # 讀取矩陣數據
    data = [list(input().strip()) for _ in range(n)]

    # 讀取 Q 個查詢點
    for _ in range(q):
        i, j = map(int, input().split())
        key = data[i][j]  # 取得查詢點的字母
        print(f(1, i, j, key, n, m, data))  # 呼叫函式計算最大正方形邊長
