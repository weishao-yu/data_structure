# PE
while True:
    try:
        name = input()
        print("Hello " + name)
    except EOFError:
        break
