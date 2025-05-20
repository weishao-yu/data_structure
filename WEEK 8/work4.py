while True:
    n = int(input())
    if n == 0:
        break
    while True:
        line = input().strip()
        if line == '0':
            print()  # 區塊結束，輸出空行
            break
        target = list(map(int, line.split()))
        stack = []
        curr = 1
        possible = True
        for num in target:
            while curr <= n and (not stack or stack[-1] != num):
                stack.append(curr)
                curr += 1
            if stack[-1] == num:
                stack.pop()
            else:
                possible = False
                break
        print('Yes' if possible else 'No')