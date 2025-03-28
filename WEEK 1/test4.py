# PG
count = 0  

while True:
    try:
        line = input().strip()
        if line == "Hello World":
            count += 1
        else:
            break
    except EOFError:
        break  

print(f"Hello World * {count}")
