def dfs(node, visited, am, n, parent):
    visited[node] = True
    for neighbor in range(n):
        if am[node][neighbor]:
            if not visited[neighbor]:
                if dfs(neighbor, visited, am, n, node):
                    return True  # 有 cycle
            elif neighbor != parent:
                return True  # 回到已訪問過且不是 parent ➝ cycle
    return False

while True:
    try:
        line = input()
        if not line:
            continue
        n = int(line)
        am = []
        for _ in range(n):
            row = list(map(int, input().split()))
            am.append(row)

        visited = [False] * n
        cycle_found = False
        components = 0

        for i in range(n):
            if not visited[i]:
                components += 1
                if dfs(i, visited, am, n, -1):
                    cycle_found = True

        edge_count = sum(sum(row) for row in am) // 2

        if not cycle_found and components == 1 and edge_count == n - 1:
            print("It is a tree.")
        elif not cycle_found and components >= 1:
            print("It is forest.")
        else:
            print("It is not a tree.")

    except EOFError:
        break
