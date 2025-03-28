while True:
    try:
        X = int(input())
        exponent = list(map(int, input().split()))

        derivative = []
        n = len(exponent) - 1
        for i in range(n):
            coefficient = exponent[i] * (n - i)
            derivative.append(coefficient)
        result = 0
        for i in range(len(derivative)):
            result += derivative[i] * (X ** (len(derivative) - 1 - i))
        print(result)
    except:
        break
