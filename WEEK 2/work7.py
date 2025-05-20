def collect_letters(T):
    letter = []        
    for i in range(T):
        x = input().strip()
        for String in x:
            if String.isalpha():
                letter.append(String.upper())
    return letter

def get_value(item):
    char, count = item
    return (-count, char)

def sorted_letters(T):
    c = {}
    x = collect_letters(T)
    for char in x:
        if char in c:
            c[char] += 1
        else:
            c[char] = 1
    sorted_items = sorted(c.items(), key=get_value)
    for key, value in sorted_items:
        print(f"{key} {value}")


while True:
    try:
        T = input().strip()
        if not T:
            continue
        T = int(T)
        sorted_letters(T)
        print()
    except EOFError:
        break

