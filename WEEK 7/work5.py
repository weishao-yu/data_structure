field_num = 1

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    # 讀地圖
    grid = [list(input()) for _ in range(n)]

    # 準備答案矩陣
    result = [['' for _ in range(m)] for _ in range(n)]

    # 所有 8 個方向
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                result[i][j] = '*'
            else:
                count = 0
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == '*':
                        count += 1
                result[i][j] = str(count)

    # 輸出
    if field_num > 1:
        print()  # 空行
    print(f"Field #{field_num}:")
    for row in result:
        print(''.join(row))
    field_num += 1
