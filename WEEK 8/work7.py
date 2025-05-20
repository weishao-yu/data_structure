n = int(input())
blocks = [[i] for i in range(n)]

def find_block(x):
    for i, stack in enumerate(blocks):
        if x in stack:
            return i, stack.index(x)
    return None, None

def return_above(i, pos):
    above = blocks[i][pos+1:]
    for b in above:
        blocks[b].append(b)
    del blocks[i][pos+1:]

while True:
    cmd = input().strip()
    if cmd == "quit":
        break
    parts = cmd.split()
    if len(parts) != 4:
        continue
    action, a, typ, b = parts
    a = int(a)
    b = int(b)
    ai, apos = find_block(a)
    bi, bpos = find_block(b)
    if ai == bi or a == b:
        continue
    if action == "move":
        return_above(ai, apos)
        if typ == "onto":
            return_above(bi, bpos)
        blocks[bi].append(blocks[ai].pop())
    elif action == "pile":
        if typ == "onto":
            return_above(bi, bpos)
        pile = blocks[ai][apos:]
        blocks[ai] = blocks[ai][:apos]
        blocks[bi].extend(pile)

for i in range(n):
    print(f"{i}:", end="")
    for b in blocks[i]:
        print(f" {b}", end="")
    print()