T = int(input())

for case_number in range(1, T+1):
    a = int(input())
    b = int(input())
    odd_sum = 0
    for i in range(a, b+1):
        if i % 2 != 0:
            odd_sum += i
    print(f'Case {case_number}: {odd_sum}')
