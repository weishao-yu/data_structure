t = int(input())
for i in range(t):
    I = int(input())
    sum = 0
    for i in range(1, I):
        if I % i == 0:
            sum += i
    
    if sum == I:
        print("Perfect")
    elif sum < I:
        print("Deficient")
    else:
        print("Abundant")