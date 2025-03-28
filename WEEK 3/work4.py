def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())

for i in range(t):
    x = input() 

    freq = {}

    for char in x:
        if char.isalnum():
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

    prime_chars = []
    for char in freq:
        if is_prime(freq[char]):
            prime_chars.append(char)

    if prime_chars:
        prime_chars.sort()
        print(f"Case {i+1}: {''.join(prime_chars)}")
    else:
        print(f"Case {i+1}: empty")



