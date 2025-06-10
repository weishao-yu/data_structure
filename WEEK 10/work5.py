while True:
    try:
        n = int(input())
        has_child = [False] * (n + 1)  # 節點編號從 1 到 n
        is_node = [False] * (n + 1)    # 標記哪些節點真的有出現過

        for _ in range(n):
            parts = list(map(int, input().split()))
            parent = parts[0]
            is_node[parent] = True
            for child in parts[1:]:
                has_child[parent] = True  # parent 有子節點
                is_node[child] = True

        leaves = []
        for i in range(1, n + 1):
            if is_node[i] and not has_child[i]:
                leaves.append(i)

        leaves.sort()
        print(" ".join(map(str, leaves)))

    except EOFError:
        break
