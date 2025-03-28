def max_cola(n):
    total = n
    empty = n

    while empty >= 3:
        new_cola = empty // 3
        total += new_cola
        empty = empty % 3 + new_cola

    if empty == 2:
        total += 1
    return total


while True:
    try:
        n = int(input())
        print(max_cola(n))
    except:
        break
