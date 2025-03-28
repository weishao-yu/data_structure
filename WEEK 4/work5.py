def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def calculate_G(N):
    G = 0
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            G += gcd(i, j)
    return G


while True:
    try:
        line = input().strip()
        if line == "0":  # 如果輸入是 0，結束程序
            break
        N = int(line)
        if 1 < N < 501:  # 確保 N 在有效範圍內
            print(calculate_G(N))
    except EOFError:
        break
