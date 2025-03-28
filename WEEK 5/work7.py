T = int(input())

for t in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    symmetric = True
    for i in range(n):
        for j in range(n):
            if matrix[i][j] < 0 or matrix[i][j] != matrix[n-1-i][n-1-j]:
                symmetric = False
                break
        if not symmetric:
            break

    result = "Symmetric" if symmetric else "Non-symmetric"
    print(f"Test #{t}: {result}")
