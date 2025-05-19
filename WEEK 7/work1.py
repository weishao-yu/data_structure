def find(sum, dif):
    a = (sum + dif) // 2
    b = (sum - dif) // 2 
    return a, b # 返回一個元組 (a, b)


n = int(input())
for i in range(n):
    sum, dif = map(int, input().split())
    if sum < dif or (sum + dif) % 2 != 0 or (sum - dif) % 2 != 0:
        print("impossible")
    else:
        a, b = find(sum, dif) # find(40, 20) 返回 (30, 10)，解包後 a = 30, b = 10
        print(a, b)