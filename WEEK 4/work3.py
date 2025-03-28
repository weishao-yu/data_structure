mp = [[-1] * 1001 for _ in range(1001)]


def s(n, m):
    if m == 0 or m > n:
        return 0
    if m == 1 or m == n:
        return 1

    if mp[n][m] == -1:
        mp[n][m] = (m * s(n - 1, m) + s(n - 1, m - 1)) % 2
    return mp[n][m]


t = int(input().strip()) 
input()  

for case in range(t):
    while True:
        line = input().strip()
        if line:  
            n, m = map(int, line.split())
            print(s(n, m))
            break

    if case < t - 1: 
        print()
