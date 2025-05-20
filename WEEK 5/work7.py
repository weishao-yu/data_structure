T = int(input())
for t in range(1, T + 1):
    line = input()
    while line.strip() == "":
        line = input()
    n = int(line.split('=')[1]) if '=' in line else int(line)
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    symmetric = True
    for i in range(n):
        for j in range(n):
            if matrix[i][j] < 0 or matrix[i][j] != matrix[n-1-i][n-1-j]:
                symmetric = False
                break
        if not symmetric:
            break
    print(f"Test #{t}: {'Symmetric.' if symmetric else 'Non-symmetric.'}")