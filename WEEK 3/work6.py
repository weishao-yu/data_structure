def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def reverse_number(n):
    return int(str(n)[::-1])

def emirp(n):
    if prime(n):
        reversed_n = reverse_number(n)
        if reversed_n !=n and prime(reversed_n):
            return True
    return False

while True:
    try:
        n = int(input())
        if emirp(n):
            print(f"{n} is emirp.")
        elif prime(n):
            print(f"{n} is prime.")
        else:
            print(f"{n} is not prime.")
    except EOFError:
        break