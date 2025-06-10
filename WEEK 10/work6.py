def preorder(tree, index, result):
    if index >= len(tree) or tree[index] == 0:
        return
    result.append(str(tree[index]))
    preorder(tree, 2 * index + 1, result)
    preorder(tree, 2 * index + 2, result)

def inorder(tree, index, result):
    if index >= len(tree) or tree[index] == 0:
        return
    inorder(tree, 2 * index + 1, result)
    result.append(str(tree[index]))
    inorder(tree, 2 * index + 2, result)

def postorder(tree, index, result):
    if index >= len(tree) or tree[index] == 0:
        return
    postorder(tree, 2 * index + 1, result)
    postorder(tree, 2 * index + 2, result)
    result.append(str(tree[index]))

first_case = True
while True:
    try:
        line = input()
        if not line:
            continue
        if not first_case:
            print()  # 多筆測資間空行
        else:
            first_case = False

        n = int(line)
        total_nodes = 2 ** n - 1
        tree = list(map(int, input().split()))
        preorder_result = []
        inorder_result = []
        postorder_result = []

        preorder(tree, 0, preorder_result)
        inorder(tree, 0, inorder_result)
        postorder(tree, 0, postorder_result)

        print(" ".join(preorder_result))
        print(" ".join(inorder_result))
        print(" ".join(postorder_result))

    except EOFError:
        break
