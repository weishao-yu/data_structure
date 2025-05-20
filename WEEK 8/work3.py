n = int(input())
for _ in range(n):
    s = input().strip()
    stack = []
    is_valid = True
    for c in s:
        if c in '([':
            stack.append(c)
        elif c == ')':
            if not stack or stack[-1] != '(':
                is_valid = False
                break
            stack.pop()
        elif c == ']':
            if not stack or stack[-1] != '[':
                is_valid = False
                break
            stack.pop()
    if is_valid and not stack:
        print('Yes')
    else:
        print('No')
