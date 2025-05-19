def solve():
    problems = int(input())
    for _ in range(problems):
        capacity, target = map(int, input().split())
        n = int(input())
        jars = [tuple(map(int, input().split())) for _ in range(n)]

        half = capacity / 2
        left = 0
        total_volume = 0
        total_heat = 0

        best_diff = float('inf')
        best_range = None

        for right in range(n):
            v, t = jars[right]
            total_volume += v
            total_heat += v * t

            # 盡量讓區間不要超過容量
            while total_volume > capacity and left <= right:
                v_l, t_l = jars[left]
                total_volume -= v_l
                total_heat -= v_l * t_l
                left += 1

            # 檢查是否符合體積與溫度限制
            if total_volume >= half:
                avg_temp = total_heat / total_volume
                if abs(avg_temp - target) <= 5:
                    diff = abs(avg_temp - target)
                    if diff < best_diff:
                        best_diff = diff
                        best_range = (left, right)

        if best_range:
            print(f"{best_range[0]} {best_range[1]}")
        else:
            print("Not possible")
solve()