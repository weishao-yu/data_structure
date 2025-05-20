def calculate_derivative(coefficients):
    derivative_coefficients = []
    degree = len(coefficients) - 1
    for i in range(degree):
        derivative = coefficients[i] * (degree - i)
        derivative_coefficients.append(derivative)
    return derivative_coefficients



while True:
    try:
        x = int(input())
        coefficients = list(map(int ,input().split()))
        derivative_coefficients = calculate_derivative(coefficients)
        sum = 0
        for i in range(len(derivative_coefficients)):
            sum += derivative_coefficients[i] * (x ** ((len(derivative_coefficients)) - 1 - i))
        print(sum)
    except EOFError:
        break
    
#coefficients 係數
