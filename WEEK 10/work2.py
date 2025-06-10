while True:
    try:
        line = input()
        if not line:
            continue
        n = int(line)
        x, y = map(int, input().split())

        # 建立圖，用普通 dict
        graph = {}
        for _ in range(n):
            parts = list(map(int, input().split()))
            u = parts[0]
            if u not in graph:
                graph[u] = []
            for v in parts[1:]:
                if v not in graph:
                    graph[v] = []
                graph[u].append(v)
                graph[v].append(u)

        # BFS 使用普通 list 模擬 queue
        visited = set()
        queue = [[x, 0]]
        found = False

        while queue:
            node, dist = queue.pop(0)
            if node == y:
                print(dist)
                found = True
                break
            if node in visited:
                continue
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append([neighbor, dist + 1])

        if not found:
            print(0)  # 樹中其實不會發生

    except EOFError:
        break
