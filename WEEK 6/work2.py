def solve():
    a = list(map(int, input().split()))
    exchange = BubbleSort(a)
    print(f"Minimum exchange operations : {exchange}")

def BubbleSort(a):
    n = len(a)
    number = 0
    while n > 1:
        n -= 1
        for i in range(n):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                number += 1
    return number
    
while True:
    try:
        n = int(input())
        solve()
    except EOFError:
        break