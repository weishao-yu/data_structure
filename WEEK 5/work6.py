def backtracking(n, length, now, idx, sticks, used, side_length):
    if length == side_length:
        now += 1
        length = 0
        idx = 0
        if now == 3:  # 三條邊都找到了，第四條邊一定能形成
            return True

    for i in range(idx, n):
        if not used[i] and length + sticks[i] <= side_length:
            used[i] = True
            if backtracking(n, length + sticks[i], now, i + 1, sticks, used, side_length):
                return True
            used[i] = False  # 回溯

            if length + sticks[i] == side_length:  # 剪枝：如果當前邊長已滿，避免重複計算
                return False

    return False


# 讀取測試案例數量
t = int(input().strip())  # 直接使用 input() 讀取

for _ in range(t):
    # 讀取木棍數量與長度
    data = list(map(int, input().split()))
    n = data[0]  # 第一個數字是 M（木棍數量）
    sticks = data[1:]  # 剩下的是木棍長度

    total_length = sum(sticks)

    # 如果總長度不是 4 的倍數，或者最大木棍長度超過邊長，直接返回 "no"
    if total_length % 4 != 0:
        print("no")
        continue

    side_length = total_length // 4
    sticks.sort(reverse=True)  # 先排序，優先放置較長的木棍
    used = [False] * n

    if sticks[0] > side_length:
        print("no")
    elif backtracking(n, 0, 0, 0, sticks, used, side_length):
        print("yes")
    else:
        print("no")
