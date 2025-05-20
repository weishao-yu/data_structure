def last_stone_weight(stones):
    stones = stones[:]  # 複製一份，避免改到原本的
    while len(stones) > 1:
        stones.sort()
        y = stones.pop()  # 最大
        x = stones.pop()  # 次大
        if x != y:
            stones.append(y - x)
    return stones[0] if stones else 0

while True:
    try:
        n = int(input())
        arr = list(map(int, input().split()))
        print(last_stone_weight(arr))
    except:
        break