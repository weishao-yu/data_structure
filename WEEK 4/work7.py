step_count = 0


def honni(n, a, b, c):
    global step_count
    if n == 1:
        step_count += 1
        print(f"Step {step_count}")
        print(f"Move disk {n} from rod {a} to rod {b}.")
    else:
        honni(n - 1, a, c, b)
        step_count += 1
        print(f"Step {step_count}")
        print(f"Move disk {n} from rod {a} to rod {b}.")
        honni(n - 1, c, b, a)


while True:
    try:
        x = int(input().strip())
        if x == 0:
            break

        step_count = 0
        honni(x, 'A', 'B', 'C')
        print()
        print(f"Total moved {step_count} steps.")
        print()
    except EOFError:
        break
