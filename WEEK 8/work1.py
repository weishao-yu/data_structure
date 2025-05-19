mod = 10**9 + 7

def f(a):
    if a == 0:
        return 1
    else:
        return a * f(a -1) % mod
    
while True:
    try:
        a = int(input())
        print(f(a))
    except EOFError:
        break