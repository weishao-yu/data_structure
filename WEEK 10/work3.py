class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1

while True:
    try:
        line = input()
        if not line:
            continue
        n = int(line)
        values = list(map(int, input().split()))
        root = None
        for v in values:
            root = insert(root, v)
        print(height(root))
    except EOFError:
        break
