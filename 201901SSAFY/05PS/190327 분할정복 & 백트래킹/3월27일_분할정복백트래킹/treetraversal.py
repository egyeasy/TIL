def inorder(T, node):
    if node != None:
        if tree[node][0] != 0:
            inorder(T, tree[node][0])
        print("- ", node, " -", end=" ")
        if tree[node][1] != 0:
            inorder(T, tree[node][1])


def preorder(T, node):
    print("- ", node, " -", end=" ")
    if tree[node][0] != 0:
        preorder(T, tree[node][0])
    if tree[node][1] != 0:
        preorder(T, tree[node][1])


def postorder(T, node):
    if tree[node][0] != 0:
        postorder(T, tree[node][0])
    if tree[node][1] != 0:
        postorder(T, tree[node][1])
    print("- ", node, " -", end=" ")


edges = 12
tree = [[0]*2 for _ in range(edges+2)]  # index : parent, tree[][0] : left child, tree[][1] : right child
inp = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

for i in range(0, edges*2, 2):
    if tree[inp[i]][0] :
        tree[inp[i]][1] = inp[i+1]
    else:
        tree[inp[i]][0] = inp[i+1]

print(tree)
print("--- preorder ----")
preorder(tree, 1)
print("\n--- inorder ----")
inorder(tree, 1)
print("\n--- postorder ----")
postorder(tree, 1)
