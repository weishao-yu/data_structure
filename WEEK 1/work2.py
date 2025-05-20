# PB
while True:
    try:
        number = input()
        if number == "0":
            break
        if number.isdigit():
            print("Hello World")       
    except EOFError:
        break
