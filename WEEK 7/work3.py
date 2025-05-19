def solve(point):
    for i in range(4):
        for j in range(i + 1, 4):
            if point[i] == point[j]:
                common = point[i]
                others = [p for k, p in enumerate(point) if k != i and k != j]
                dx = others[0][0] - common[0]
                dy = others[0][1] - common[1]
                another = (others[1][0] + dx, others[1][1] + dy)
                return another




while True:
    try:
        line = input()
        nums = list(map(float, line.strip().split()))
        point = [(nums[i], nums[i+1]) for i in range(0 , 8, 2)]
        result = solve(point)
        print(f"{result[0]:.3f} {result[1]:.3f}")
    except EOFError:
        break 

