n = int(input())
stack = []

for _ in range(n):
    query = input().strip()
    if query.startswith('Sleep'):
        _, name = query.split()
        stack.append(name)
    elif query == 'Kick':
        if stack:
            stack.pop()
    elif query == 'Test':
        if stack:
            print(stack[-1])
        else:
            print('Not in a dream')
