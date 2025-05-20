while True:
    n = int(input())
    if n == 0:
        break
    cards = list(range(1, n+1))
    discarded = []
    while len(cards) > 1:
        discarded.append(cards.pop(0))
        cards.append(cards.pop(0))
    print("Discarded cards:", end="")
    if discarded:
        print(" " + ", ".join(map(str, discarded)))
    else:
        print()
    print(f"Remaining card: {cards[0]}")