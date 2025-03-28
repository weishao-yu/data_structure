def multiply_9(x):
    result = 0
    i = 0
    while x > 0:
        result = result + x % 10
        x = x // 10
    return result


def is_multiple_of_9(x):
    sum_digits = multiply_9(x)
    degree = 1
    while sum_digits >= 10:
        sum_digits = multiply_9(sum_digits)
        degree += 1
    return sum_digits == 9, degree


while True:
    x = int(input())
    if x == 0:
        break
    is_multiple, degree = is_multiple_of_9(x)
    if is_multiple:
        print(f"{x} is a multiple of 9 and has 9-degree {degree}.")
    else:
        print(f"{x} is not a multiple of 9.")
