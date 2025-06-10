while True:
    try:
        line = input()
        if not line:
            continue
        n, x, y = map(int, line.strip().split())

        parent = {}
        nodes = set()
        children = set()

        for _ in range(n):
            parts = list(map(int, input().strip().split()))
            root = parts[0]
            nodes.add(root)
            for child in parts[1:]:
                parent[child] = root
                children.add(child)
                nodes.add(child)

        # 找出 root（沒被當過子節點）
        root_node = (nodes - children).pop()

        def get_ancestors(node):
            ancestors = []
            while node in parent:
                ancestors.append(node)
                node = parent[node]
            ancestors.append(node)  # 加入 root
            return ancestors[::-1]

        ax = get_ancestors(x)
        ay = get_ancestors(y)

        # 找 LCA
        lca = root_node
        for u, v in zip(ax, ay):
            if u == v:
                lca = u
            else:
                break

        print(lca)

    except EOFError:
        break
