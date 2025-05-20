T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))
    queue = [(i, p) for i, p in enumerate(priorities)]
    count = 0
    while queue:
        idx, pri = queue.pop(0)
        if any(pri < other[1] for other in queue):
            queue.append((idx, pri))
        else:
            count += 1
            if idx == m:
                print(count)
                break